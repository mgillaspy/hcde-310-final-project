# Create an instance of Flask
from flask import Flask, render_template, request
from functions import search_by_ingredient_safe, get_recipe_details, get_meal_instructions, get_meal_name, get_meal_image, get_nutritional_information
app = Flask(__name__)

# Create a view function for /
@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

# Create a view function for /results
@app.route("/results", methods=['GET','POST'])
def results():

    if request.method == 'POST':
        ingredient = request.form['ingredient']

        results = search_by_ingredient_safe(ingredient) # this is a list of meal dictionaries with requested ingredient
        meal_ids_lst = []
        #for meal in matching_meals:
            # access the meal id
            # add that meal's id to meal_ids_lst
    return render_template('results.html', ingredient=ingredient, results=results) # add all necessary parameters, meal_ids_list = meal_ids_lst)


if __name__ == "__main__":
    print("Starting the Flask app...")
    app.run(debug=True)