import sys
path = r'ubuntu/home/flask'
if path not in sys.path:
    sys.path.append(path)
import library


from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/question')
def query(question):
    response = library.query(question)
    return response

if __name__ == '__main__':
    app.run(debug=True)

