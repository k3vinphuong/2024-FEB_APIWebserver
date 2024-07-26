from datetime import date

from flask import Blueprint

from init import db, bcrypt
from models.user import User
from models.meal import Meal
from models.fooditem import Fooditem

db_commands = Blueprint("db", __name__)

@db_commands.cli.command("create")
def create_tables():
    db.create_all()
    print("Tables created")

@db_commands.cli.command("drop")
def drop_tables():
    db.drop_all()
    print("Tables dropped")

@db_commands.cli.command("seed")
def seed_tables():
    users = [
        User(
            email="admin@email.com",
            password=bcrypt.generate_password_hash("Hello1234").decode("utf=8"),
            is_admin=True
        ),
        User(
            name="User 1",
            email="user1@email.com",
            password=bcrypt.generate_password_hash("Hello1234").decode("utf=8"),
        )
    ]

    db.session.add_all(users)

    meals = [
        Meal(
           meal_name="Banana Honey Smoothie",
           meal_time = date.today(),
           total_protein="13g",
           total_calorie="352kcal", 
        ),

        Meal(
           meal_name="French Toast With Eggs",
           meal_time = date.today(),
           total_protein="15g",
           total_calorie="235kcal", 
        ),

        Meal(
           meal_name="Peanut Butter And Banana Sandwich",
           meal_time = date.today(),
           total_protein="35g",
           total_calorie="930kcal", 
        ),
        
        Meal(
           meal_name="Lobster Mac and Cheese",
           meal_time = date.today(),
           total_protein="34g",
           total_calorie="731kcal", 
        ),

        Meal(
           meal_name="Rigatoni Sausage Bake",
           meal_time = date.today(),
           total_protein="31g",
           total_calorie="749kcal", 
        ),
    ]
    db.session.add_all(meals)

    food_items = [
        Fooditem(
            name="Banana",
            protein_content="1g",
            calorie_content="110cal",
            serving_size="1",
        ),

        Fooditem(
            name="Eggs",
            protein_content="6.3g",
            calorie_content="74cal",
            serving_size="1",
        ),

        Fooditem(
            name="Peanut Butter",
            protein_content="8g",
            calorie_content="190cal",
            serving_size="2 tbsp",
        ),

        Fooditem(
            name="Lobster",
            protein_content="27g",
            calorie_content="128cal",
            serving_size="145g",
        ),

        Fooditem(
            name="Australian Pork Sausage",
            protein_content="10.2g",
            calorie_content="134cal",
            serving_size="75g",
        ),

        Fooditem(
            name="French Toast",
            protein_content="5g",
            calorie_content="149cal",
            serving_size="65g",
        ),
    ]
    db.session.add_all(food_items)

    db.session.commit()

    print("Tables seeded")
