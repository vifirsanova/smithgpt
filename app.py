from flask import Flask, render_template, request, jsonify
import os, io, docx, PyPDF2, json, chardet, toml
from werkzeug.utils import secure_filename
from pathlib import Path

app = Flask(__name__)

def load_config():
    with open('config.toml', 'r') as f:
        return toml.load(f)

config = load_config()

app.config['MAX_CONTENT_LENGTH'] = config['max_content_length']

ALLOWED_EXTENSIONS = set(config['extensions'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_ipynb_content(file_stream):
    """Extract code and markdown cells from Jupyter notebook in memory"""
    try:
        notebook = json.load(file_stream)
        content = []
        for cell in notebook.get('cells', []):
            if cell['cell_type'] == 'code':
                content.append(f"# Code Cell:\n{''.join(cell['source'])}")
            elif cell['cell_type'] == 'markdown':
                content.append(f"# Markdown Cell:\n{''.join(cell['source'])}")
        return '\n\n'.join(content)
    except Exception as e:
        return f"Error parsing notebook: {str(e)}"

def extract_text_from_file(file_stream, filename):
    try:
        extension = os.path.splitext(filename)[1].lower()
        
        # Handle Word documents
        if extension in ('.doc', '.docx'):
            doc = docx.Document(io.BytesIO(file_stream.read()))
            return '\n'.join([para.text for para in doc.paragraphs])
        
        # Handle PDFs
        elif extension == '.pdf':
            reader = PyPDF2.PdfReader(io.BytesIO(file_stream.read()))
            text = '\n'.join([page.extract_text() for page in reader.pages])
            return text
        
        # Handle Jupyter Notebooks
        elif extension == '.ipynb':
            return extract_ipynb_content(io.TextIOWrapper(file_stream, encoding='utf-8'))
        
        # Handle all other text-based files
        else:
            raw_data = file_stream.read(1024)
            file_stream.seek(0)
            result = chardet.detect(raw_data)
            encoding = result['encoding'] or 'utf-8'
            text_content = io.TextIOWrapper(file_stream, encoding=encoding).read()
            return text_content
    
    except UnicodeDecodeError:
        return "This file appears to be binary. Only text-based files are supported."
    except Exception as e:
        return f"Error extracting text: {str(e)}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        try:
            content = extract_text_from_file(file.stream, file.filename)
            return jsonify({
                'filename': secure_filename(file.filename),
                'content': content
            })
        except Exception as e:
            return jsonify({'error': f"Processing error: {str(e)}"}), 500
    else:
        return jsonify({'error': 'File type not allowed'}), 400

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    message = data.get('message', '').strip()
    
    if not message:
        return jsonify({'error': 'Empty message'}), 400
    
    return jsonify({
        'response': f"I received your message: '{message}'. This is a placeholder response."
    })

if __name__ == '__main__':
    app.run(debug=True)
