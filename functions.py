import urllib.parse, urllib.request, urllib.error, json
from keys import API_KEY
import requests

# MealDB Functions

# Search meals by ingredient (returns a JSON with meals and their name, image, and id)
def search_by_ingredient(ingredient) :
    baseurl = "https://www.themealdb.com/api/json/v1/" + API_KEY + "/filter.php"
    parameter = {"i": ingredient}
    paramstr = urllib.parse.urlencode(parameter)
    meal_ingd_request = baseurl + "?" + paramstr

    try:
        meal_ingd_response_str = urllib.request.urlopen(meal_ingd_request).read()
        meal_ingd_data = json.loads(meal_ingd_response_str)
        return meal_ingd_data.get("meals", [])  # Returns list of meal dictionaries or empty list
    except Exception as e:
        print(f"Error fetching meals for ingredient {ingredient}: {e}")
        return []

# Accesses more detailed recipe information by meal ID that's not given by the filter by ingredient JSON response
def get_recipe_details(meal_id) :
    baseurl = "https://www.themealdb.com/api/json/v1/" + API_KEY + "/lookup.php"
    parameter = {"i": meal_id}
    paramstr = urllib.parse.urlencode(parameter)
    meal_id_request = baseurl + "?" + paramstr

    try:
        meal_id_response_str = urllib.request.urlopen(meal_id_request).read()
        meal_id_data = json.loads(meal_id_response_str)
        return meal_id_data.get("meals", [])[0]  # Return the first meal dictionary or empty dict
    except Exception as e:
        print(f"Error fetching recipe details for meal ID {meal_id}: {e}")
        return {}


# Safely search by ingredient with error handling
def search_by_ingredient_safe(ingredient) :
    try:
        return search_by_ingredient(ingredient)
    except urllib.error.URLError as e:
        print(f"Network error: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []
