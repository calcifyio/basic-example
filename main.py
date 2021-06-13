from flask import Flask
import numpy as np
import torch
import subprocess
app = Flask(__name__)

@app.route('/')
def hello_calcfiy():
    n = np.random.randn()
    output = subprocess.check_output(['nvidia-smi'], shell=True).decode()
    lines = output.split('\n')
    html = 'CUDA: ' + str(torch.cuda.is_available()) + '</br>'
    for line in lines:
        html += '<div>' + line + '</div>'
    return html
