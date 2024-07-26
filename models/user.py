from init import db, ma
from marshmallow import fields
from marshmallow.validate import Regexp

class User(db.Model):
    __tablename__ = "users"

    # structure of table, each column
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    # email needs to be unique and cannot be null
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable = False)
    date_of_birth = db.Column(db.Date)
    gender = db.Column(db.String)
    height = db.Column(db.Float, nullable = False)
    weight = db.Column(db.Float, nullable = False)
    # by default users are not admins
    is_admin = db.Column(db.Boolean, default=False)
    
    meals = db.relationship('Meal', back_populates="user")

# user schema, provided by marshmallow
class UserSchema(ma.Schema):
    meals = fields.List(fields.Nested('MealSchema', exclude=["user"]))

    email = fields.String(required=True, validate=Regexp("^\S+@\S+\.\S+$", error="Invalid Email Format"))

    password = fields.String(required=True, validate=Regexp("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", error="Minimum eight characters, at least one letter and one number"))
    
    class Meta:
        fields = ( "user_id", "username", "email", "password", "date_of_birth", "gender", "height", "weight", "is_admin", "meals", )

# schema to handle one user
user_schema = UserSchema(exclude=["password"])
#schema to handle multiple users
users_schema = UserSchema(many=True, exclude=["password"])

