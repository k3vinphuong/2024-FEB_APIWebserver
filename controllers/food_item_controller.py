from datetime import  date

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.fooditem import Fooditem, food_item_schema, food_items_schema

food_item_bp = Blueprint("fooditems", __name__, url_prefix="/fooditems")

@food_item_bp.route("/")
def get_all_food_items():
    stmt = db.select()