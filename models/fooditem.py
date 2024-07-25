from init import db, ma
from marshmallow import fields

class Fooditem(db.Model):
    __tablename__ = "fooditems"

    food_item_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    protein_content = db.Column(db.Float, nullable=False)
    calorie_content = db.Column(db.Float, nullable=False)
    serving_size = db.Column(db.Integer)

    mealitem = db.relationship("Mealitem", back_populates="fooditem")

    class FoodItemSchema(ma.Schema):
        
        mealitem = fields.Nested("MealItemSchema", only=["quantity"])

        class Meta:
            fields = ("food_item_id", "name", "protein_content", "calorie_content", "serving_size", "meal_item")

    food_item_schema = FoodItemSchema()
    food_items_schema = FoodItemSchema(many=True)