import urllib.parse, urllib.request, urllib.error, json
import pprint
from keys import API_KEY, APP_ID
from keys import APP_ID


def search_by_ingredient(ingredient):

    baseurl = "www.themealdb.com/api/json/v1/1/filter.php"

    # if input ingredient contains space, make that space into an underscore for the API to recognize it
        # e.g., chicken breast --> chicken_breast

    # only parameter for this API function is the name of the ingredient
    parameter = {
        "i": ingredient
    }

    # load the json data
    paramstr = urllib.parse.urlencode(parameter)
    meal_ingd_request = baseurl + '?' + paramstr
    meal_ingd_response_str = urllib.request.urlopen(meal_ingd_request).read()
    meal_ingd_data = json.loads(meal_ingd_response_str)

    # use the json to get the matching meals
    meals_with_ingredient = meal_ingd_data["meals"] # This will be a list of meal_dictionaries
    return meals_with_ingredient



# because the filter by ingredient function returns a dictionary with has name, image, and id
def get_recipe_details(meal_id):
    baseurl = "www.themealdb.com/api/json/v1/1/lookup.php"
    parameter = {
        "i": meal_id
    }

    paramstr = urllib.parse.urlencode(parameter)
    meal_id_request = baseurl + '?' + paramstr
    meal_id_response_str = urllib.request.urlopen(meal_id_request).read()
    meal_id_data = json.loads(meal_id_response_str)

    meal_with_id = meal_id_data[0]  # This will be a list with one item's dictionary, the meal with the requested id
    return meal_with_id

    # add a function to get the meal name, instructions, and image list using meal_id
def get_meal_name(meal_with_id):
    meal_with_id["meals"][0]["strMeal"]

def get_meal_instructions(meal_with_id):
    meal_with_id["meals"][0]["strInstructions"]

def get_meal_image(meal_with_id):
    meal_with_id["meals"][0]["strMealThumb"]


# catches errors within search_by_ingredient, either executing the code or returning an error message
def search_by_ingredient_safe(ingredient):
    try:
        return search_by_ingredient(ingredient)
    except ConnectionError:
        print("Error trying to retrieve data. Failed to reach the server.")
        return None
    except TypeError:
        print(f"No meals found with " + ingredient + ". Try another search.") #empty list of meals/no matching meals found in DB
        return None # do I need these None's?
    except Exception as e:
        print("Error trying to retrieve data:", e)
    return None



# Use Nutritionix API to get more nutritional information for these different meals.
def get_nutritional_information(meal):
    baseurl = "https://trackapi.nutritionix.com/v2/search/instant"

    paramstr = {
        "query": meal
    }

    # Headers with authentication
    headers = {
        "x-app-id": APP_ID,
        "x-app-key": API_KEY
    }

    #paramstr = urllib.parse.urlencode(parameter)
    #meal_nutr_request = baseurl + '?' + paramstr
    #meal_nutr_response_str = urllib.request.urlopen(meal_nutr_request).read()
    #meal_nutr_data = json.loads(meal_nutr_response_str)

    response = requests.get(meal_nutr_request, headers=headers, params=paramstr)

    if response.status_code == 200:
        data = response.json()
        print("Nutritional Data for Apple:", data)
    else:
        print("Error:", response.status_code, response.text)

