from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# Create tables if they don't exist
with app.app_context():
    db.create_all()


@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy", "message": "Service is up and running"}), 200


if __name__ == "__main__":
    app.run(debug=True)
