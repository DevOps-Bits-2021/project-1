# To Access OS environmental variables
import os

# Library for API calls
import requests
headers = {
    'content-type': "application/json",
    'x-rapidapi-key': "e4e39f869amsh5c0528bc0d8320cp18ca39jsn5fa8e07ba8df",
    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
}
# headers = {}


def recipe_search(recipe_search, number_of_results, exclude):
    """Extracts recipe search results from Spoonacular API."""
    print(recipe_search)
    # Set up parameters for API call, then call Spoonacular API

    payload = {'query': recipe_search, 'number': number_of_results, "excludeIngredients": exclude}
    spoonacular_endpoint = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search'
    response = requests.get(spoonacular_endpoint,
                            params=payload,
                            headers=headers)
    print(response.json()['results'])
    return response.json()


def summary_info(recipe_id):
    # call Spoonacular API, inserting recipe_id into endpoint
    summary_response = (requests.get(
        'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/' + recipe_id + '/summary', headers=headers))
    return summary_response.json()


def recipe_info(recipe_id):
    # example_recipe_info = {
    #                               "vegetarian": False,
    #                               "vegan": False,
    #                               "glutenFree": False,
    #                               "dairyFree": False,
    #                               "veryHealthy": False,
    #                               "cheap": False,
    #                               "veryPopular": True,
    #                               "sustainable": False,
    #                               "weightWatcherSmartPoints": 13,
    #                               "gaps": "no",
    #                               "lowFodmap": False,
    #                               "ketogenic": False,
    #                               "whole30": False,
    #                               "servings": 6,
    #                               "preparationMinutes": 10,
    #                               "cookingMinutes": 30,
    #                               "sourceUrl": "http://www.twopeasandtheirpod.com/italian-sausage-tortellini-soup/",
    #                               "spoonacularSourceUrl": "https://spoonacular.com/italian-sausage-tortellini-soup-548180",
    #                               "aggregateLikes": 82923,
    #                               "spoonacularScore": 97,
    #                               "healthScore": 28,
    #                               "creditText": "Two Peas and Their Pod",
    #                               "sourceName": "Two Peas and Their Pod",
    #                               "pricePerServing": 265.78,
    #                               "extendedIngredients": [
    #                                 {
    #                                   "id": 2004,
    #                                   "aisle": "Spices and Seasonings",
    #                                   "image": "https://spoonacular.com/cdn/ingredients_100x100/bay-leaves.jpg",
    #                                   "consistency": "solid",
    #                                   "name": "bay leaf",
    #                                   "amount": 1,
    #                                   "unit": "",
    #                                   "unitShort": "",
    #                                   "unitLong": "",
    #                                   "originalString": "1 bay leaf",
    #                                   "metaInformation": []
    #                                 },
    #                                 {
    #                                   "id": 11531,
    #                                   "aisle": "Canned and Jarred",
    #                                   "image": "https://spoonacular.com/cdn/ingredients_100x100/tomatoes-canned.jpg",
    #                                   "consistency": "solid",
    #                                   "name": "canned diced tomatoes",
    #                                   "amount": 30,
    #                                   "unit": "ounce",
    #                                   "unitShort": "oz",
    #                                   "unitLong": "ounces",
    #                                   "originalString": "2 (15 ounce) cans diced tomatoes",
    #                                   "metaInformation": [
    #                                     "diced",
    #                                     "canned"
    #                                   ]
    #                                 },
    #                                 {
    #                                   "id": 10093727,
    #                                   "aisle": "Refrigerated",
    #                                   "image": "https://spoonacular.com/cdn/ingredients_100x100/tortellini-isolated.jpg",
    #                                   "consistency": "solid",
    #                                   "name": "cheese tortellini",
    #                                   "amount": 2,
    #                                   "unit": "cups",
    #                                   "unitShort": "cup",
    #                                   "unitLong": "cups",
    #                                   "originalString": "2 cups cheese tortellini (fresh or frozen)",
    #                                   "metaInformation": [
    #                                     "fresh",
    #                                     "()"
    #                                   ]
    #                                 },
    #                                 {
    #                                   "id": 6194,
    #                                   "aisle": "Canned and Jarred",
    #                                   "image": "https://spoonacular.com/cdn/ingredients_100x100/chicken-broth.png",
    #                                   "consistency": "liquid",
    #                                   "name": "chicken broth",
    #                                   "amount": 8,
    #                                   "unit": "cups",
    #                                   "unitShort": "cup",
    #                                   "unitLong": "cups",
    #                                   "originalString": "8 cups vegetable or chicken broth",
    #                                   "metaInformation": []
    #                                 },
    #                                 {
    #                                   "id": 2044,
    #                                   "aisle": "Produce;Spices and Seasonings",
    #                                   "image": "https://spoonacular.com/cdn/ingredients_100x100/basil.jpg",
    #                                   "consistency": "solid",
    #                                   "name": "fresh basil",
    #                                   "amount": 0.25,
    #                                   "unit": "cup",
    #                                   "unitShort": "cup",
    #                                   "unitLong": "cups",
    #                                   "originalString": "1/4 cup chopped fresh basil",
    #                                   "metaInformation": [
    #                                     "fresh",
    #                                     "chopped"
    #                                   ]
    #                                 },
    #                                 {
    #                                   "id": 11215,
    #                                   "aisle": "Produce",
    #                                   "image": "https://spoonacular.com/cdn/ingredients_100x100/garlic.jpg",
    #                                   "consistency": "solid",
    #                                   "name": "garlic",
    #                                   "amount": 3,
    #                                   "unit": "cloves",
    #                                   "unitShort": "cloves",
    #                                   "unitLong": "cloves",
    #                                   "originalString": "3 cloves garlic, minced",
    #                                   "metaInformation": [
    #                                     "minced"
    #                                   ]
    #                                 },
    #                                 {
    #                                   "id": 7036,
    #                                   "aisle": "Meat",
    #                                   "image": "https://spoonacular.com/cdn/ingredients_100x100/italian-sausage.jpg",
    #                                   "consistency": "solid",
    #                                   "name": "italian sausage",
    #                                   "amount": 1,
    #                                   "unit": "lb",
    #                                   "unitShort": "lb",
    #                                   "unitLong": "pound",
    #                                   "originalString": "1 lb. Italian Sausage, rolled into 1/4 teaspoon size balls",
    #                                   "metaInformation": [
    #                                     "italian"
    #                                   ]
    #                                 },
    #                                 {
    #                                   "id": 11233,
    #                                   "aisle": "Produce",
    #                                   "image": "https://spoonacular.com/cdn/ingredients_100x100/kale.jpg",
    #                                   "consistency": "solid",
    #                                   "name": "kale",
    #                                   "amount": 1.5,
    #                                   "unit": "cups",
    #                                   "unitShort": "cup",
    #                                   "unitLong": "cups",
    #                                   "originalString": "1 1/2 cups chopped kale",
    #                                   "metaInformation": [
    #                                     "chopped"
    #                                   ]
    #                                 },
    #                                 {
    #                                   "id": 4053,
    #                                   "aisle": "Oil, Vinegar, Salad Dressing",
    #                                   "image": "https://spoonacular.com/cdn/ingredients_100x100/olive-oil.jpg",
    #                                   "consistency": "liquid",
    #                                   "name": "olive oil",
    #                                   "amount": 1,
    #                                   "unit": "tablespoon",
    #                                   "unitShort": "Tbsp",
    #                                   "unitLong": "tablespoon",
    #                                   "originalString": "1 tablespoon olive oil",
    #                                   "metaInformation": []
    #                                 },
    #                                 {
    #                                   "id": 11282,
    #                                   "aisle": "Produce",
    #                                   "image": "https://spoonacular.com/cdn/ingredients_100x100/brown-onion.jpg",
    #                                   "consistency": "solid",
    #                                   "name": "onion",
    #                                   "amount": 1,
    #                                   "unit": "",
    #                                   "unitShort": "",
    #                                   "unitLong": "",
    #                                   "originalString": "1 small onion, diced",
    #                                   "metaInformation": [
    #                                     "diced",
    #                                     "small"
    #                                   ]
    #                                 },
    #                                 {
    #                                   "id": 11821,
    #                                   "aisle": "Produce",
    #                                   "image": "https://spoonacular.com/cdn/ingredients_100x100/red-bell-pepper.png",
    #                                   "consistency": "solid",
    #                                   "name": "red bell peppers",
    #                                   "amount": 2,
    #                                   "unit": "",
    #                                   "unitShort": "",
    #                                   "unitLong": "",
    #                                   "originalString": "2 red bell peppers, diced",
    #                                   "metaInformation": [
    #                                     "diced",
    #                                     "red"
    #                                   ]
    #                                 },
    #                                 {
    #                                   "id": 1032009,
    #                                   "aisle": "Spices and Seasonings",
    #                                   "image": "https://spoonacular.com/cdn/ingredients_100x100/red-pepper-flakes.jpg",
    #                                   "consistency": "solid",
    #                                   "name": "red pepper flakes",
    #                                   "amount": 0.125,
    #                                   "unit": "teaspoon",
    #                                   "unitShort": "tsp",
    #                                   "unitLong": "teaspoons",
    #                                   "originalString": "1/8 teaspoon red pepper flakes",
    #                                   "metaInformation": [
    #                                     "red"
    #                                   ]
    #                                 },
    #                                 {
    #                                   "id": 1102047,
    #                                   "aisle": "Spices and Seasonings",
    #                                   "image": "https://spoonacular.com/cdn/ingredients_100x100/salt-and-pepper.jpg",
    #                                   "consistency": "solid",
    #                                   "name": "salt and pepper",
    #                                   "amount": 6,
    #                                   "unit": "servings",
    #                                   "unitShort": "servings",
    #                                   "unitLong": "servings",
    #                                   "originalString": "Salt and black pepper, to taste",
    #                                   "metaInformation": [
    #                                     "black",
    #                                     "to taste"
    #                                   ]
    #                                 }
    #                               ],
    #                               "id": 548180,
    #                               "title": "Italian Sausage Tortellini Soup",
    #                               "readyInMinutes": 40,
    #                               "image": "https://spoonacular.com/recipeImages/548180-556x370.jpg",
    #                               "imageType": "jpg",
    #                               "cuisines": [
    #                                 "mediterranean",
    #                                 "european",
    #                                 "italian"
    #                               ],
    #                               "dishTypes": [
    #                                 "lunch",
    #                                 "soup",
    #                                 "main course",
    #                                 "main dish",
    #                                 "dinner"
    #                               ],
    #                               "diets": [],
    #                               "instructions": "1. In a large skillet, brown the mini sausage balls until cooked through. This will take about 5-7 minutes. Drain off the grease and place the sausage balls on a plate lined with paper towels.2. In a large pot, heat the olive oil over medium high heat. Add the onion and cook until tender, 3-4 minutes. Stir in the garlic and cook for 2 minutes. Stir in the red peppers, bay leaf, and red pepper flakes. Cook until peppers are soft, about 3 minutes. 3. Stir in the broth, tomatoes, and kale. Add the cheese tortellini and cook until tortellini is tender, 7-8 minutes. Stir in the fresh basil and season with salt and pepper, to taste. Stir in the mini sausage balls and heat until warm. Remove the bay leaf and serve.Note-you can make this soup vegetarian by using vegetable broth and omitting the sausage. Josh always ladles up my bowl first, and then adds the sausage. This soup recipe is very adaptable!",
    #                               "analyzedInstructions": [
    #                                 {
    #                                   "name": "",
    #                                   "steps": [
    #                                     {
    #                                       "number": 1,
    #                                       "step": "In a large skillet, brown the mini sausage balls until cooked through. This will take about 5-7 minutes.",
    #                                       "ingredients": [],
    #                                       "equipment": [
    #                                         {
    #                                           "id": 404645,
    #                                           "name": "frying pan",
    #                                           "image": "https://spoonacular.com/cdn/equipment_100x100/pan.png"
    #                                         }
    #                                       ],
    #                                       "length": {
    #                                         "number": 7,
    #                                         "unit": "minutes"
    #                                       }
    #                                     },
    #                                     {
    #                                       "number": 2,
    #                                       "step": "Drain off the grease and place the sausage balls on a plate lined with paper towels.2. In a large pot, heat the olive oil over medium high heat.",
    #                                       "ingredients": [
    #                                         {
    #                                           "id": 4053,
    #                                           "name": "olive oil",
    #                                           "image": "https://spoonacular.com/cdn/ingredients_100x100/olive-oil.jpg"
    #                                         }
    #                                       ],
    #                                       "equipment": [
    #                                         {
    #                                           "id": 405895,
    #                                           "name": "paper towels",
    #                                           "image": "https://spoonacular.com/cdn/equipment_100x100/paper-towels.jpg"
    #                                         },
    #                                         {
    #                                           "id": 404752,
    #                                           "name": "pot",
    #                                           "image": "https://spoonacular.com/cdn/equipment_100x100/stock-pot.jpg"
    #                                         }
    #                                       ]
    #                                     },
    #                                     {
    #                                       "number": 3,
    #                                       "step": "Add the onion and cook until tender, 3-4 minutes. Stir in the garlic and cook for 2 minutes. Stir in the red peppers, bay leaf, and red pepper flakes. Cook until peppers are soft, about 3 minutes. 3. Stir in the broth, tomatoes, and kale.",
    #                                       "ingredients": [
    #                                         {
    #                                           "id": 1032009,
    #                                           "name": "red pepper flakes",
    #                                           "image": "https://spoonacular.com/cdn/ingredients_100x100/red-pepper-flakes.jpg"
    #                                         },
    #                                         {
    #                                           "id": 11821,
    #                                           "name": "red pepper",
    #                                           "image": "https://spoonacular.com/cdn/ingredients_100x100/red-bell-pepper.png"
    #                                         },
    #                                         {
    #                                           "id": 2004,
    #                                           "name": "bay leaves",
    #                                           "image": "https://spoonacular.com/cdn/ingredients_100x100/bay-leaves.jpg"
    #                                         },
    #                                         {
    #                                           "id": 11215,
    #                                           "name": "garlic",
    #                                           "image": "https://spoonacular.com/cdn/ingredients_100x100/garlic.jpg"
    #                                         },
    #                                         {
    #                                           "id": 11282,
    #                                           "name": "onion",
    #                                           "image": "https://spoonacular.com/cdn/ingredients_100x100/brown-onion.jpg"
    #                                         },
    #                                         {
    #                                           "id": 11233,
    #                                           "name": "kale",
    #                                           "image": "https://spoonacular.com/cdn/ingredients_100x100/kale.jpg"
    #                                         }
    #                                       ],
    #                                       "equipment": [],
    #                                       "length": {
    #                                         "number": 9,
    #                                         "unit": "minutes"
    #                                       }
    #                                     },
    #                                     {
    #                                       "number": 4,
    #                                       "step": "Add the cheese tortellini and cook until tortellini is tender, 7-8 minutes. Stir in the fresh basil and season with salt and pepper, to taste. Stir in the mini sausage balls and heat until warm.",
    #                                       "ingredients": [
    #                                         {
    #                                           "id": 10093727,
    #                                           "name": "cheese tortellini",
    #                                           "image": "https://spoonacular.com/cdn/ingredients_100x100/tortellini-isolated.jpg"
    #                                         },
    #                                         {
    #                                           "id": 1102047,
    #                                           "name": "salt and pepper",
    #                                           "image": "https://spoonacular.com/cdn/ingredients_100x100/salt-and-pepper.jpg"
    #                                         },
    #                                         {
    #                                           "id": 2044,
    #                                           "name": "fresh basil",
    #                                           "image": "https://spoonacular.com/cdn/ingredients_100x100/fresh-basil.jpg"
    #                                         },
    #                                         {
    #                                           "id": 93727,
    #                                           "name": "tortellini",
    #                                           "image": "https://spoonacular.com/cdn/ingredients_100x100/tortellini-isolated.jpg"
    #                                         }
    #                                       ],
    #                                       "equipment": [],
    #                                       "length": {
    #                                         "number": 8,
    #                                         "unit": "minutes"
    #                                       }
    #                                     },
    #                                     {
    #                                       "number": 5,
    #                                       "step": "Remove the bay leaf and serve.Note-you can make this soup vegetarian by using vegetable broth and omitting the sausage. Josh always ladles up my bowl first, and then adds the sausage. This soup recipe is very adaptable!",
    #                                       "ingredients": [
    #                                         {
    #                                           "id": 2004,
    #                                           "name": "bay leaves",
    #                                           "image": "https://spoonacular.com/cdn/ingredients_100x100/bay-leaves.jpg"
    #                                         }
    #                                       ],
    #                                       "equipment": [
    #                                         {
    #                                           "id": 404630,
    #                                           "name": "ladle",
    #                                           "image": "https://spoonacular.com/cdn/equipment_100x100/ladle.jpg"
    #                                         },
    #                                         {
    #                                           "id": 404783,
    #                                           "name": "bowl",
    #                                           "image": "https://spoonacular.com/cdn/equipment_100x100/bowl.jpg"
    #                                         }
    #                                       ]
    #                                     }
    #                                   ]
    #                                 }
    #                               ]
    #                             }

    # return example_recipe_info
    querystring = {"includeNutrition":"true"}
    info_response = requests.get(
         'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/'
         + recipe_id + '/information', headers=headers, params=querystring )
    
    return info_response.json()


# def some_function(payload):
#     url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/visualizeRecipe'
#     headers['content-type'] = 'multipart/form-data; boundary=---011000010111000001101001'
#     response = requests.request("POST", url, data=payload, headers=headers)
#     return response


def recommend_diet_based_on_cals1(target_calories, exclude, default_time="day"):

    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/mealplans/generate"
    query_string = {
        "timeFrame": default_time,
        "targetCalories": target_calories,
        "diet": "vegan",
        "exclude": exclude

    }
    response = requests.request(
        "GET", url, headers=headers, params=query_string)
    # response = response.text

    # response = {"meals":
    # [{"id":596996,"imageType":"jpg","title":"Homemade Vanilla Extract","readyInMinutes":5,"servings":2,"sourceUrl":"http://leitesculinaria.com/82842/recipes-homemade-vanilla-extract.html"},
    # {"id":249642,"imageType":"jpg","title":"Giraffeâ€™s Love No-Bake Vegan Cheesecake","readyInMinutes":30,"servings":8,"sourceUrl":"http://www.godairyfree.org/recipes/giraffes-love-no-bake-vegan-qcheesecakeq-too"},{"id":647638,"imageType":"jpg","title":"Hummus Wrap With Carrots and Cucumbers","readyInMinutes":45,"servings":1,"sourceUrl":"https://spoonacular.com/hummus-wrap-with-carrots-and-cucumbers-647638"}],"nutrients":{"calories":2827.57,"protein":57.14,"fat":106.51,"carbohydrates":174.23}}

    return response.json()


def recommend_diet_based_on_cals2(target_calories, exclude, default_time="day"):

    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/mealplans/generate"
    query_string = {
        "timeFrame": default_time,
        "targetCalories": target_calories,
        "diet": "keto",
        "exclude": exclude

    }
    response = requests.request(
        "GET", url, headers=headers, params=query_string)
    # response = response.text

    # response = {"meals":[{"id":1177043,"imageType":"jpg","title":"Overnight Blueberry Banana Cheesecake Oats","readyInMinutes":120,"servings":4,"sourceUrl":"https://slimfast.com/recipes/overnight-blueberry-cheesecake-oats/"},{"id":1102572,"imageType":"jpg","title":"Steak and Scallops with Lime-Dill Hollandaise","readyInMinutes":30,"servings":2,"sourceUrl":"https://cookingwithcurls.com/2019/04/05/steak-and-scallops-with-lime-dill-hollandaise/"},{"id":73587,"imageType":"jpg","title":"Coffee-Marinated Bison Short Ribs","readyInMinutes":45,"servings":6,"sourceUrl":"http://www.epicurious.com/recipes/food/views/Coffee-Marinated-Bison-Short-Ribs-241342"}],"nutrients":{"calories":2694.66,"protein":150.58,"fat":174.22,"carbohydrates":141.75}}
    return response.json()


def recommend_diet_based_on_cals3(target_calories,exclude, default_time="day"):

    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/mealplans/generate"
    query_string = {
        "timeFrame": default_time,
        "targetCalories": target_calories,
        "diet": "gluten free",
        "exclude": exclude

    }
    response = requests.request(
        "GET", url, headers=headers, params=query_string)
    #response = response.text

    # response = {"meals":[{"id":625935,"imageType":"jpg","title":"5 Ingredient Triple Decker Chocolate Peanut Butter Bars","readyInMinutes":45,"servings":16,"sourceUrl":"https://www.halfbakedharvest.com/5-ingredient-tripple-decker-chocolate-peanut-butter-bars/"},{"id":989730,"imageType":"jpg","title":"One Pan Skillet Honey Dijon Chicken","readyInMinutes":30,"servings":4,"sourceUrl":"https://www.lecremedelacrumb.com/one-pan-skillet-honey-dijon-chicken"},{"id":357733,"imageType":"jpeg","title":"Roasted Free Range Chicken","readyInMinutes":585,"servings":4,"sourceUrl":"http://www.foodnetwork.com/recipes/roasted-free-range-chicken-recipe.html"}],"nutrients":{"calories":2507.16,"protein":115.89,"fat":195.45,"carbohydrates":68.42}}
    return response.json()

def search_by_pantry(ingredient_list, num_ops=7):
    
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients"
    querystring = {
        "ingredients": ingredient_list,
        "number": num_ops,
    }
    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.json()