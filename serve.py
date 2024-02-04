from flask import Flask, request, jsonify
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['POST'])
def run_stress_test():
    subprocess.Popen(['python3', 'stress_cpu.py'])
    return jsonify({"status": "CPU stress test started"}), 202

@app.route('/', methods=['GET'])
def get_private_ip():
    hostname = socket.gethostname()
    private_ip = socket.gethostbyname(hostname)
    return jsonify({"private_ip": private_ip})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
