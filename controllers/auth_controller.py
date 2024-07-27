from datetime import timedelta

from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from init import bcrypt, db
from models.user import User, user_schema, UserSchema
from utils import auth_as_admin_decorator

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/register", methods=["POST"])
def register_user():
    try:
        # the data we get in body of request
        body_data = UserSchema().load(request.get_json())
        
        # create the user instance
        user = User(
            username=body_data.get("username"),
            email=body_data.get("email"),
            height=body_data.get("height"),
            weight=body_data.get("weight")
        )
        
        # password from request body
        password = body_data.get("password")
       
        # if password exist, hash password
        if password:
            user.password = bcrypt.generate_password_hash(password).decode("utf-8")
        
        # add and commit the user to DB
        db.session.add(user)
        db.session.commit()
        
        # respond back to client
        return user_schema.dump(user), 201
    
    except IntegrityError as err:
        if err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
            return {"error": f"The column {err.orig.diag.column_name} is required"}, 409
        if err.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
            return {"error": "Email address already in use"}, 409
        

@auth_bp.route("/login", methods=["POST"])
def login_user():
    # get data from request body
    body_data = request.get_json()
    # find user with email address
    stmt = db.select(User).filter_by(email=body_data.get("email"))
    user = db.session.scalar(stmt)
    # if user and password is correct
    if user and bcrypt.check_password_hash(user.password, body_data.get("password")):
        # create json web token
        token = create_access_token(identity=str(user.id), expires_delta=timedelta(days=1))
        # return the token with user info
        return {"email": user.email, "is_admin": user.is_admin, "token": token}
    # else
    else:
        # return error
        return {"error": "Invalid email or password"}, 401
    
@auth_bp.route("/users/<int:user_id>", methods=["PUT", "PATCH"])
@jwt_required()
def update_user(user_id):
    body_data = UserSchema().load(request.get_json(), partial=True)
    password = body_data.get("password")
    stmt = db.select(User).filter_by(id=get_jwt_identity())
    user = db.session.scalar(stmt)
    if user:
        user.name = body_data.get("name") or user.name
        if password:
            user.password = bcrypt.generate_password_hash(password).decode("utf-8")
        db.session.commit()
        return user_schema.dump(user)
    else:
        return {"error": "user does not exist"}, 404
    
@auth_bp.route("/users/<int:user_id>", methods=["DELETE"])
@jwt_required()
@auth_as_admin_decorator
def delete_user(user_id):
    # find the user with id from DB
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    # if user exist
    if user:
        # delete the user
        db.session.delete(user)
        db.session.commit
        # return a message
        return {"message": f"User with id {user_id} deleted"}
    # else
    else:
        # return error saying user doesnt exist
        return {"error": f"User with id {user_id} not found"}, 404