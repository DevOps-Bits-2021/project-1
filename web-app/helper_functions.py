""" SQL Alchemy queries used for Flask routes. """

# Import model.py table definitions
from app.models import User, Recipe, Ingredient, List, Cuisine, PantryList
from app.models import RecipeIngredient, ListIngredient, Bookmark, RecipeCuisine, Planner

# Password hashing library

# Import file with all the Spoonacular API calls
from app import api_calls,db


def check_if_user_exists(username):
    """Checks if user exists in DB. If so, returns instantiated User
    object. Returns none if user not found."""

    return User.query.filter(User.username == username).first()


def check_if_list_exists(user_id, list_name):
    """Check if list exists in DB. If so, returns instantiated List
    object. Returns none if list not found."""

    return List.query.filter((List.list_name == list_name) &
                             (List.user_id == user_id)).first()


def check_if_recipe_exists(recipe_id):
    """Check if recipe exists in DB. If so, returns instantiated Recipe object.
    Returns none if recipe not found."""

    return Recipe.query.filter(Recipe.recipe_id == recipe_id).first()


def check_if_bookmark_exists(recipe_id, user_id):
    """Check if bookmark exists in DB. If so, returns instantiated Bookmark
    object. Returns none if bookmark not found."""

    return Bookmark.query.filter((Bookmark.recipe_id == recipe_id) &
                                 (Bookmark.user_id == user_id)).first()

def check_if_meal_exists_in_planner(recipe_id, user_id):
    """Check if bookmark exists in DB. If so, returns instantiated Bookmark
    object. Returns none if bookmark not found."""

    return Planner.query.filter((Planner.recipe_id == recipe_id) &
                                 (Planner.user_id == user_id)).first()



def check_if_ingredient_exists(ingredient_id):
    """Check if ingredient exists in DB. If so, returns instantiated Ingredient
    object. Returns none if ingredient not found."""

    return Ingredient.query.filter(Ingredient.ing_id == ingredient_id).first()



def check_if_cuisine_exists(cuisine_name):
    """Check if cuisine exists in DB. If so, returns instantiated Cuisine
    object. Returns none if cuisne not found."""

    return Cuisine.query.filter(Cuisine.cuisine_name == cuisine_name).first()




def add_recipe_ingredient(recipe_id, ing_id, meas_unit, mass_qty):
    """Adds recipe's ingredient to RecipeIngredient table in DB."""

    new_recipe_ingredient = RecipeIngredient(recipe_id=recipe_id,
                                             ing_id=ing_id,
                                             meas_unit=meas_unit,
                                             mass_qty=mass_qty)

    db.session.add(new_recipe_ingredient)
    db.session.commit()

    return new_recipe_ingredient


def add_ingredients(recipe_id, ingredients_info):
    """Adds recipe's ingredients to Ingredient table in DB. This in turn
    also requires adding ingredient's aisles to Aisle table and populating
    RecipeIngredient table."""

    # Loop through ing. list, adding new ingredients and aisles to DB if necessary
    for ingredient_info in ingredients_info:
        ingredient_id = str(ingredient_info['id'])
        ingredient_exists = check_if_ingredient_exists(ingredient_id)

        if not ingredient_exists:
            # create Ingredient object that may or may not have aisle id info
            new_ingredient = Ingredient(ing_id=ingredient_id,
                                        ing_name=ingredient_info['name'])

           

            # At this point, new_ingredient should have an aisle_id
            # Add completed new_ingredient to DB
            db.session.add(new_ingredient)
            db.session.commit()

            # Add new ing to RecipeIngredient table
            add_recipe_ingredient(recipe_id,
                                  ingredient_id,
                                  ingredient_info['unit'],
                                  ingredient_info['amount'])
        else:
            # Add already-existing ing to RecipeIngredient table, since this is
            # always going to be a new recipe (indicated in server.py conditional).
            # This ing could already exist in DB due to past recipes using the
            # same ingredient.
            add_recipe_ingredient(recipe_id,
                                  ingredient_id,
                                  ingredient_info['unit'],
                                  ingredient_info['amount'])


def add_recipe_cuisine(cuisine_id, recipe_id):
    """Populates RecipeCuisine association table in DB after adding
    Cuisine to DB."""

    new_recipe_cuisine = RecipeCuisine(cuisine_id=cuisine_id, recipe_id=recipe_id)
    db.session.add(new_recipe_cuisine)
    db.session.commit()


def add_cuisines(recipe_id, cuisines):
    """Adds cuisines to Cuisine table in DB."""

    for cuisine in cuisines:
        cuisine_exists = check_if_cuisine_exists(cuisine)

        if not cuisine_exists:
            new_cuisine = Cuisine(cuisine_name=cuisine)
            db.session.add(new_cuisine)
            db.session.commit()
            cuisine_id = new_cuisine.cuisine_id
        else:
            cuisine_id = cuisine_exists.cuisine_id
        add_recipe_cuisine(cuisine_id, recipe_id)


def add_recipe(recipe_id,current_user):
    """ Adds recipe to Recipes table, which also populates the following
    tables: Ingredient, Aisle, Cuisine, RecipeIngredient. Returns new Recipe
    object back to server."""

    # Get info from API and store as json
    info_response = api_calls.recipe_info(recipe_id)

    # Add new recipe to DB
    new_recipe = Recipe(recipe_id=recipe_id,
                        recipe_name=info_response['title'],
                        img_url=info_response['image'],
                        instructions=info_response['instructions'],
                        user_id=current_user.id)

    db.session.add(new_recipe)
    db.session.commit()

    # Isolate ingredients and cuisine info from dict to be added to DB.
    ingredients_info = info_response['extendedIngredients']
    add_ingredients(recipe_id, ingredients_info)

    cuisines = info_response['cuisines']
    add_cuisines(recipe_id, cuisines)

    return new_recipe




def add_bookmark(user_id, recipe_id):
    """Adds recipe to Bookmarks table. Returns instantiated Bookmark object."""

    new_bookmark = Bookmark(user_id=user_id, recipe_id=recipe_id)

    db.session.add(new_bookmark)
    db.session.commit()

    return new_bookmark


def add_meal(user_id, recipe_id, recipe_cals):
    """Adds recipe to Planner table. Returns instantiated Planner object."""

    new_meal = Planner(user_id=user_id, recipe_id=recipe_id, recipe_cals=recipe_cals)

    db.session.add(new_meal)
    db.session.commit()
    print("Added successfully")
    return new_meal


def add_new_list(user_id, list_name):
    """Adds new list to List table."""
    print("new list added")

    new_list = List(user_id=user_id, list_name=list_name)
    print("new list added")
    db.session.add(new_list)
    db.session.commit()

    return new_list


def add_to_list(recipe_id, list_id):
    """ Add chosen recipe's ingredients to ListIngredient table in DB. Return
    a list of ListIngredient objects. """

    # Get list of recipe_ingredient objects that have ing_ids, meas, and units
    recipe_ingredients = (RecipeIngredient.query
                          .filter(RecipeIngredient.recipe_id == recipe_id)
                          .all()
                          )

    # Create empty list, which will be appended with new ListIngredient objects
    updated_list_ingredients = []

    for recipe_ingredient in recipe_ingredients:
        new_ListIngredient = ListIngredient(list_id=list_id,
                                            ing_id=recipe_ingredient.ing_id,
                                            meas_unit=recipe_ingredient.meas_unit,
                                            mass_qty=recipe_ingredient.mass_qty)
        db.session.add(new_ListIngredient)
        db.session.commit()
        updated_list_ingredients.append(new_ListIngredient)

    # Return the list of ListIngredient objects
    return updated_list_ingredients

pantrylist = []

def add_to_pantry(user_id, ing_name):
    """This function adds the ingredient to pantry for the given user

    Args:
        user_id (integer): the id of the user whose pantry list it is
        ing_name (str): the name of the ingredient to be displayed

    Returns:
        [list]: list of items in the users pantry
    """
    print("item added to pantry")
    # pantrylist = []
    new_item = PantryList(user_id=user_id, ing_name=ing_name)
    db.session.add(new_item)
    db.session.commit()
    pantrylist.append(ing_name)
    return pantrylist

def delete_from_pantry(user_id, ing_name):
    print("item deleted from pantry")
    del_item = PantryList.query.filter_by(ing_name=ing_name).first()
    pantrylist.remove(ing_name)
    db.session.delete(del_item)
    db.session.commit()
    return pantrylist

