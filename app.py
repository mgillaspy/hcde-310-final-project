# Import necessary modules and functions
from flask import Flask, render_template, request
from functions import (
    search_by_ingredient_safe,
    get_recipe_details,
)

# Create an instance of Flask
app = Flask(__name__)

# Home route
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# Results route
@app.route("/results", methods=["GET", "POST"])
def results():
    if request.method == "POST":
        ingredient = request.form.get("ingredient", "").strip()

        if not ingredient:
            error_message = "Please enter a valid ingredient."
            return render_template("index.html", error_message=error_message)

        # Get meal results from MealDB
        results = search_by_ingredient_safe(ingredient)
        if not results:
            error_message = f"No meals found with the ingredient '{ingredient}'."
            return render_template("index.html", error_message=error_message)

        # Make a list to store meal details
        full_meal_info = []
        for meal in results:
            meal_name = meal["strMeal"]
            meal_id = meal["idMeal"]
            meal_details = get_recipe_details(meal_id)

            full_meal_info.append({
                "name": meal_name,
                "id": meal_id,
                "image": meal["strMealThumb"],
                "area": meal_details.get("strArea"),
                "category": meal_details.get("strCategory"),
                "instructions": meal_details.get("strInstructions", ""),
            })

        # Pass the data to the template
        return render_template("results.html", ingredient=ingredient, meals=full_meal_info)

    return render_template("index.html")

# Simpler way to run the Flask app
if __name__ == "__main__":
    print("Starting the Flask app...")
    app.run(debug=True)
#
