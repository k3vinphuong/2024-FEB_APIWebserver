from init import db, ma
from marshmallow import fields

class Fooditem(db.Model):
    __tablename__ = "fooditems"

    food_item_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    protein_content = db.Column(db.Float, nullable=False)
    calorie_content = db.Column(db.Float, nullable=False)
    serving_size = db.Column(db.Integer)

    meal_id = db.Column(db.Integer, db.ForeignKey("meals.id"), nullable=False)

    meal = db.relationship("Meal", back_populates="food_items")

class FoodItemSchema(ma.Schema):

    class Meta:
        fields = ("food_item_id", "name", "protein_content", "calorie_content", "serving_size", "meal")
        ordered = True

food_item_schema = FoodItemSchema()
food_items_schema = FoodItemSchema(many=True)