document.addEventListener('DOMContentLoaded', function() {
    const chatForm = document.getElementById('chat-form');
    const userInput = document.getElementById('user-input');
    const chatMessages = document.getElementById('chat-messages');
    const fileInput = document.getElementById('file-input');
    const sendButton = document.querySelector('.send-button');
    
    userInput.addEventListener('input', function() {
        this.style.height = 'auto';
        this.style.height = (this.scrollHeight) + 'px';
        alignInputWithButtons();
    });
    
    function alignInputWithButtons() {
        const inputHeight = userInput.scrollHeight;
        document.querySelectorAll('.file-input-button, .send-button').forEach(button => {
            button.style.height = `${Math.max(36, inputHeight)}px`;
        });
    }
    
    chatForm.addEventListener('submit', function(e) {
        e.preventDefault();
        sendMessage();
    });
    
    userInput.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });
    
    fileInput.addEventListener('change', function() {
        if (this.files && this.files[0]) {
            const file = this.files[0];
            addMessage(`[Uploading: ${file.name}]`, 'user');
            
            const formData = new FormData();
            formData.append('file', file);
            
            fetch('/upload', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    addMessage(`Error: ${data.error}`, 'bot');
                } else {
                    addMessage(`${data.content}`, 'bot');
                }
            })
            .catch(error => {
                addMessage(`Upload failed: ${error.message}`, 'bot');
            });
            
            this.value = '';
        }
    });
    
    function sendMessage() {
        const message = userInput.value.trim();
        
        if (message) {
            addMessage(message, 'user');
            userInput.value = '';
            userInput.style.height = 'auto';
            alignInputWithButtons();
            
            fetch('/send_message', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message })
            })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    addMessage(`Error: ${data.error}`, 'bot');
                } else {
                    addMessage(data.response, 'bot');
                }
            })
            .catch(error => {
                addMessage("Sorry, there was an error processing your message.", 'bot');
            });
        }
    }
    
    function addMessage(text, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message');
        messageDiv.classList.add(sender === 'bot' ? 'bot-message' : 'user-message');
        
        const formattedText = document.createElement('pre');
        formattedText.style.margin = '0';
        formattedText.style.fontFamily = 'inherit';
        formattedText.style.whiteSpace = 'pre-wrap';
        formattedText.textContent = text;
        
        messageDiv.appendChild(formattedText);
        messageDiv.setAttribute('role', sender === 'bot' ? 'status' : 'log');
        
        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
    
    alignInputWithButtons();
});
