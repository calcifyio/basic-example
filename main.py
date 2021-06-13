from flask import Flask
import numpy as np
import subprocess
app = Flask(__name__)

@app.route('/')
def hello_calcfiy():
    n = np.random.randn()
    output = subprocess.check_output(['nvidia-smi'], shell=True).decode()
    lines = output.split('\n')
    html = 'Hello, Calcify New ' + str(n) + '</br>'
    for line in lines:
        html += '<div>' + line + '</div>'
    return html
