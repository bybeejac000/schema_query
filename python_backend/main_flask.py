import sys
path = r'/home/ubuntu/schema_query/python_backend'
if path not in sys.path:
    sys.path.append(path)
import library

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/question', methods=['POST'])
def query():
    data = request.get_json()
    question = data.get('prompt')
    response = library.query(question)
    return jsonify({'response': response})



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)


