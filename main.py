import os

from flask import Flask
from marshmallow.exceptions import ValidationError

from init import db, ma, bcrypt, jwt

def create_app():
    app = Flask(__name__)

    app.json.sort_keys = False

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")

    app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    @app.errorhandler(ValidationError)
    def validation_error(err):
        return {"error": err.messages}, 400
    
    @app.errorhandler(400)
    def bad_request(err):
        return {"error": err.messages}, 400
    
    @app.errorhandler(401)
    def unauthenicated():
        return {"error": "You are not authenticated"}, 401

    from controllers.cli_controller import db_commands
    app.register_blueprint(db_commands)
    
    from controllers.auth_controller import auth_bp
    app.register_blueprint(auth_bp)

    from controllers.meal_controller import meals_bp
    app.register_blueprint(meals_bp)
    
    from controllers.food_item_controller import food_item_bp
    app.register_blueprint(food_item_bp)

    return app