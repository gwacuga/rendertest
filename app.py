import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Python Hosting is Working 🚀"

if __name__ == "__main__":
    # Get the port from Render environment variable, default to 5000
    port = int(os.environ.get("PORT", 5000))
    # Bind to 0.0.0.0 so Render can access it externally
    app.run(host="0.0.0.0", port=port)
