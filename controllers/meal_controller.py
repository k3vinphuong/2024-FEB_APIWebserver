from datetime import date

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.meal import Meal, meal_schema, meals_schema

meals_bp = Blueprint("meals", __name__, url_prefix="/meals")

@meals_bp.route("/")
def get_all_meals():
    stmt = db.select(Meal).order_by(Meal.date.desc())
    meals = db.session.scalars(stmt)
    return meals_schema.dump(meals)

@meals_bp.route("/<int:meal_id>")
def get_one_meal(meal_id):
    stmt = db.select(Meal).filter_by(id=meal_id)
    meal = db.session.scalar(stmt)
    if meal:
        return meal_schema.dump(meal)
    else:
        return {"error": f"Card with id {meal_id} not found"}, 404
    
@meals_bp.route("/", methods=["POST"])
@jwt_required()
def create_meal():
    body_data = request.get_json()
    # Create a new meal model instance
    meal = Meal(
        title=body_data.get("movie_title"),
        time=date.today(),
        protein=body_data.get("total_protein"),
        calorie=body_data.get("total_calorie"),
        user_id=get_jwt_identity()
    )
    # add that to the session and commit
    db.session.add(meal)
    db.session.commit()
    # return the newly created meal
    return meal_schema.dump(meal)


@meals_bp.route("/<int:meal_id>", methods=["DELETE"])
@jwt_required()
def delete_meal(meal_id):
    # get the meal from the DB
    stmt = db.select(Meal).filter_by(id=meal_id)
    meal = db.session.scalar(stmt)
    # if meal exists
    if meal:
        # delete the meal from the session and commit
        db.session.delete(meal)
        db.session.commit()
        return {"message": f"Meal '{meal.title}' deleted successfully"}
    # else
    else:
        # return error message
        return {"error": f"Meal with id {meal_id} not found"}, 404 


@meals_bp.route("/<int:meal_id>", methods=["PUT", "PATCH"])
@jwt_required()
def update_meal(meal_id):
    # Get the data to be updated from body of request
    body_data = request.get_json
    # get the meal from the DB whose field needs to be update
    stmt = db.select(Meal).filter_by(id=meal_id)
    meal = db.session.scalar(stmt)
   # if meal exists
    if meal:
        # update the fields as required
        meal.title = body_data.get("title") or meal.title
        meal.total_protein = body_data.get("total_protein") or meal.total_protein
        meal.total_calorie = body_data.get("total_calorie") or meal.total_calorie
        
        # commit to the DB
        db.session.commit()
        # return the update meal back
        return meal_schema.dump(meal)
    # else
    else:
        # return error message
        return {"error": f"Movie with id {"movie_id"} not found"}
    