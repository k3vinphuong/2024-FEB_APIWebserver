from init import db, ma 
from marshmallow import fields

class Meal(db.Model):
    __tablename__ = "meals"

    meal_id = db.Column(db.Integer, primary_key=True)
    movie_title = db.Cloumn(db.String, unqiue=True)
    meal_time = db.Column(db.Date) # When it was eaten
    total_protein = db.Column(db.Float, nullable=False)
    total_calorie = db.Column(db.Float, nullable=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    user = db.relationship('User', back_populates='meals')

class MealSchema(ma.Schema):
    
    user = fields.Nested('UserSchema', only=["id", "name", "email"])

    class Meta:
        fields = ( "meal_id", "user", "meal_time", "total_protein", "total_calories" )

meal_schema = MealSchema()
meals_schema = MealSchema(many=True)
