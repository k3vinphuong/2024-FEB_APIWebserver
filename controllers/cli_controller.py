from datetime import date

from flask import Blueprint

from init import db, bcrypt
from models.user import User
from models.meal import Meal

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
    db.session.commit()

    print("Tables seeded")
