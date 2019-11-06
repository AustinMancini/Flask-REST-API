from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
# ma = Marshmallow()

def create_app(config_filename):
    app = Flask(__name__)
    
    app.config.from_object(config_filename)

    db.init_app(app)

    from app import api_bp
    app.register_blueprint(api_bp)

    return app

if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True)
