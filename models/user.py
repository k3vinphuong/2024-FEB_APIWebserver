from init import db, ma
from marshmallow import fields

class User(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable = False)
    date_of_birth = db.Column(db.Date)
    gender = db.Column(db.String)
    height = db.Column(db.Float, nullable = False)
    weight = db.Column(db.Float, nullable = False)
    
    meals = db.relationship('Meal', back_populates="user")

class UserSchema(ma.Schema):
    meals = fields.List(fields.Nested('MealSchema', exclude=["user"]))
    class Meta:
        fields = ( "user_id", "username", "email", "password", "dateofbirth", "gender", "height", "weight", "is_admin", "meals" )

user_schema = UserSchema(exclude=["password"])
users_schema = UserSchema(many=True, exclude=["password"])

