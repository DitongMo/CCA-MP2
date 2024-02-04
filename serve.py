from flask import Flask, request
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    hostname = socket.gethostname()
    private_ip = socket.gethostbyname(hostname)
    return private_ip

@app.route('/', methods=['POST'])
def stress_cpu():
    subprocess.Popen(["python3", "stress_cpu.py"])
    return 'CPU stress started', 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
