from init import db, ma 
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp

class Meal(db.Model):
    __tablename__ = "meals"

    id = db.Column(db.Integer, primary_key=True)
    meal_name = db.Column(db.String, unique=True)
    meal_time = db.Column(db.Date) # When it was eaten
    total_protein = db.Column(db.Integer, nullable=False)
    total_calorie = db.Column(db.Integer, nullable=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    user = db.relationship("User", back_populates="meals")
    food_items = db.relationship("Fooditem", back_populates="meal")

class MealSchema(ma.Schema):
    
    user = fields.Nested('UserSchema', only=["id", "name", "email"])
    
    meal_name = fields.String(required=True, validate=And(
        Length(min=2, error="Title must be at least 2 characters long"),
        Regexp('^[A-Za-z0-9 ]+$', error="Title must have alphanumerics characters only")
    ))

    class Meta:
        fields = ( "id", "meal_name", "meal_time", "total_protein", "total_calories", "user", "food_item" )
        ordered = True

meal_schema = MealSchema()
meals_schema = MealSchema(many=True)
