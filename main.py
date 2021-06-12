from flask import Flask
import subprocess
app = Flask(__name__)

@app.route('/')
def hello_calcfiy():
    output = subprocess.check_output(['nvidia-smi'], shell=True).decode()
    lines = output.split('\n')
    html = 'Hello, Calcify v12</br>'
    for line in lines:
        html += '<div>' + line + '</div>'
    return html
