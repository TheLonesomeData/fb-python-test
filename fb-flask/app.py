from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
# Enable CORS for all routes with more specific settings
CORS(
    app,
    resources={
        r"/*": {
            "origins": "*",
            "methods": ["GET", "POST", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"],
        }
    },
)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name}


# Create tables if they don't exist
with app.app_context():
    db.create_all()


@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy", "message": "Service is up and running"}), 200


@app.route("/authors", methods=["POST", "OPTIONS"])
@app.route("/authors/", methods=["POST", "OPTIONS"])
def create_author():
    if request.method == "OPTIONS":
        # Handle preflight request
        response = app.make_default_options_response()
        return response

    # Handle POST request
    data = request.get_json()

    if not data or "name" not in data:
        return jsonify({"error": "Name is required"}), 400

    author = Author(name=data["name"])
    db.session.add(author)
    db.session.commit()

    return jsonify(author.to_dict()), 201


# get authors

# create blog post

# get blog posts

# get blog post by id


if __name__ == "__main__":
    app.run(debug=True)
