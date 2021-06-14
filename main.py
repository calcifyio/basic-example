from flask import Flask
import torch
import subprocess
app = Flask(__name__)

@app.route('/')
def hello_calcfiy():
    output = subprocess.check_output(['nvidia-smi'], shell=True).decode()
    lines = output.split('\n')
    html = 'DEV PyTorch CUDA:' + str(torch.cuda.is_available()) + '</br>'
    for line in lines:
        html += '<div>' + line + '</div>'
    return html
