from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "✅ Flask app deployed via GitHub Actions, Docker, and Kubernetes!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
