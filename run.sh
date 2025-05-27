#!/bin/bash
pip install -r requirements.txt --break-system-packages

quantization="False"

while [[ $# -gt 0 ]]; do
    case "$1" in
        --quantization)
            quantization="$2"
            shift 2
            ;;
        *)
            echo "Unknown argument: $1"
            exit 1
            ;;
    esac
done

if [[ "$quantization" != "True" && "$quantization" != "False" ]]; then
    echo "Error: --quantization must be either 'True' or 'False'"
    exit 1
fi

python3 app.py --quantization "$quantization"
