from flask import Flask

app = Flask(__name__)

# to test: http://127.0.0.1:5000/api/v1/hello-world-16

@app.route('/api/v1/hello-world-16')
def hello_world():
    return "Hello World 16", 200

if __name__ == '__main__':
    app.run(debug=True)
