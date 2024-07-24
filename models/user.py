from init import db, ma

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable = False)
    dateofbirth = db.Column(db.Integer)
    gender = db.Column(db.String)
    height = db.Column(db.Integer, nullable = False)
    weight = db.Cloumn(db.Integer, nullable = False)
    is_admin = db.Column(db.Boolean, default = False)
    
class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "username", "email", "password", "dateofbirth", "gender", "height", "weight", "is_admin")


user_schema = UserSchema(exclude=["password"])

users_schema = UserSchema(many=True, exclude=["password"])

