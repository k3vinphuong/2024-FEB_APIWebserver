from datetime import  date

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.fooditem import Fooditem, food_item_schema, food_items_schema
from models.meal import Meal

food_item_bp = Blueprint("food_items", __name__, url_prefix="/<int:meal_id>/food_items")

@food_item_bp.route("/", methods=["POST"])
@jwt_required()
def create_food_item(meal_id):
    body_data = request.get_json()
    stmt = db.select(Meal).filter_by(id=meal_id)
    meal = db.session.scalar(stmt)

    if meal:
        food_item = Fooditem(
           food_item_name=body_data.get("message"),
           date=date.today,
           meal=meal,
           user_id=get_jwt_identity(),
        )
        db.session.add(food_item)
        db.session.commit()
        return food_item_schema.dump(food_item), 201
    else:
        return {"error": f"Meal with id {meal_id} doesn't exist"}, 404

@food_item_bp.route("/<int:food_items_id>", methods=["DELETE"])
@jwt_required()
def delete_food_item(meal_id, food_item_id):
    stmt = db.select(Fooditem).filter_by(id=food_item_id)
    food_item = db.session.scalar(stmt)
    if food_item:
        db.session.delete(food_item)
        db.session.commit()
        return {"message": f"Food item '{food_item.message} deleted successfully"}
    else:
        return {"error": f"Food item with id {food_item_id} not found"}, 404
    
@food_item_bp.route("/<int:food_items_id", methods=["PUT", "PATCH"])
@jwt_required()
def edit_food_item(meal_id, food_item_id):
    body_data = request.get_json()
    stmt = db.select(Fooditem).filter_by(id=food_item_id)
    food_item = db.session.scalar(stmt)
    if food_item:
        food_item.message - body_data.get("message") or food_item.message
        db.session.commit()
        return food_item_schema.dump(food_item)
    else:
        return {"error" f"Food item with id {food_item_id} not found in meal with id {meal_id}"}, 404