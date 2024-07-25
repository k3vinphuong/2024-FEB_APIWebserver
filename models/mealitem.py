from init import db, ma
from marshmallow import fields

class Mealitem(db.Model):
    __tablename___ = "meal_items"

    meal_item_id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)

    meal_id = db.Column(db.Intger, db.ForeignKey("meal_id"), nullable=False)
    food_item_id = db.Column(db.Integer, db.ForeignKey("food_item_id"), nullable=False)

    meal = db.relationship('Meal', back_populates="mealitem")
    fooditem = db.relationship("Fooditem", back_populates="mealitem")

class MealItemSchema(ma.Schema):
    
    class Meta:
        fields = ("meal_item_id", "food_item_id", "quantity")

meal_item_schema = MealItemSchema()
meal_items_schema = MealItemSchema(many=True)