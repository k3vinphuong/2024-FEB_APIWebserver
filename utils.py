import functools

from flask_jwt_extended import get_jwt_identity

from init import db
from models.user import User

def authorise_as_admin():
    # get the user's id
    user_id = get_jwt_identity()
    # fetch the user from the db
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    # check whether user is an admin
    return user.is_admin

def auth_as_admin_decorator(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        # get users id from get_jwt_identity
        user_id = get_jwt_identity()
        # get user using id
        stmt = db.select(User).filter_by(id=user_id)
        user = db.session.scalar(stmt)
        # if user is admin
        if user.is_admin:
            # allow dcorated function to execute
            return fn(*args, **kwargs)
        # else
        else:
            # return error
            return {"error": "Admin only"}, 403

    return wrapper