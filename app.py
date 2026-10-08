from flask import Flask

app = Flask(__name__)

# Intentional scanner test finding: fake hardcoded password.
password = "test-password-123"

# Intentional scanner test finding: fake hardcoded API key.
api_key = "fake-api-key-123456"

# Normal values that should not be reported as secrets.
username = "demo-user"
port = 5000
debug = False


@app.get("/")
def home():
    return "Security Scanner Test Application"


if __name__ == "__main__":
    app.run(host="localhost", port=port, debug=debug)
