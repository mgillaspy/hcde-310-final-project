**HCDE 310 - Explanation of Project Changes**

With the change in requirements as well as difficulties getting access to certain API’s (namely Pinterest), I shifted my project to focus on implementing just one API (the MealDB), and I decided to take out my calls to the Nutritionix API. Initially my app idea was to allow users to search for any meal and see both the instructions and nutritional information about those meals all aggregated on one page. However, I’ve now updated it to focus less on giving users access to nutritional information about different meals, and more on allowing users to search for meals based on a certain ingredient and receive information (such as ingredients, category, etc.) about those meals.

To give an example, any user can now type in an ingredient (e.g. “chicken”), and receive cards with images and names of meals using those ingredients. They can then click on a dropdown below each meal image and name to access more information about individual meals, including the instructions on how to make it, and the area from which the meal originated.

_Note: The MealDB did not require an individual API key. I simply used “1”, as I was using the API for educational purposes. See here for more details: https://www.themealdb.com/api.php._
