from flask import Flask, render_template
from routes import register_routes
import os

# Create a Flask app
app = Flask(__name__)

# Set a secret key
app.config["SECRET_KEY"] = "your_random_secret_key"
app.config["UPLOAD_FOLDER"] = "notes"
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)


# Register routes
register_routes(app)


if __name__ == "__main__":
    app.run(debug=True)
