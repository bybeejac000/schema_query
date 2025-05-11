from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/update', methods=['POST'])
def update():
    subprocess.run(['git', 'pull'], cwd='/home/ubuntu/schema_query/python_backend')
    return 'Updated!', 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6000)
