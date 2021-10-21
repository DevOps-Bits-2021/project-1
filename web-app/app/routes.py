from app import app
from flask import request
from flask import render_template, flash, redirect, url_for, request, g, session
from app.forms import LoginForm
from flask_login import logout_user
from flask_login import current_user, login_user, login_required
from werkzeug.urls import url_parse
from app.models import Ingredient, List, PantryList, Planner, Recipe, RecipeLocal, User
from app import db
from app.forms import AddRecipeForm, EditProfileForm, PantryForm, PantrySearch, RegistrationForm

from app import api_calls
import helper_functions


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        user = User.query.filter_by(id=current_user.id).first()
        exclude = user.exclude
        result = request.form
        recipe_search = result['top-search']
        results_json = api_calls.recipe_search(recipe_search, 6, exclude)
        print(results_json)

        for recipe in results_json['results']:
            recipe_id = str(recipe['id'])
            summary_response = api_calls.summary_info(recipe_id)
            summary_json = summary_response
            summary_text = summary_json['summary']
            recipe['summary'] = summary_text
            recipe['imgUrl'] = results_json['baseUri'] + recipe['image']
        result = results_json['results']
        return render_template('catagory-post.html', result=result)
    else:
        return render_template('index.html')

@app.route('/')
@app.route('/index2', methods=['GET', 'POST'])
def index2():
   
    # recipe_search = ['flour','butter','sugar']
    
    forsend = PantryList.query.filter_by(user_id=current_user.id).all()
    
    send = ''
    for item in forsend:
        send+(item.ing_name.upper())
        send=send+','+(item.ing_name.upper())
    
    results_json = api_calls.search_by_pantry(send, 6)
   
    print(results_json)

    for recipe in results_json:
        recipe_id = str(recipe['id'])
        summary_response = api_calls.summary_info(recipe_id)
        summary_json = summary_response
        summary_text = summary_json['summary']
        recipe['summary'] = summary_text
        recipe['imgUrl'] = recipe['image']
    result = results_json
    return render_template('catagory-post.html', result=result)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=False)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data,  dob=form.dob.data, name=form.name.data,
                    height=form.height.data, weight=form.weight.data, gender=form.gender.data, activity_f=form.activity_f.data, exclude=form.exclude.data)
        user.set_password(form.password.data)
        user.set_age(form.dob.data, form.weight.data, form.height.data,
                     form.gender.data, form.activity_f.data, form.wt_choice.data)
        db.session.add(user)
        db.session.commit()
        # flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/user/add-recipe', methods=["GET", "POST"])
@login_required
def addrecipe():
    form = AddRecipeForm()
    if request.method == 'POST' and form.validate_on_submit():
        recipe = RecipeLocal(recipe_name=form.name.data, ing_name=form.ingredients.data,
                             instructions=form.instructions.data, user_id=current_user.id)
        db.session.add(recipe)
        db.session.commit()
        flash('You added a recipe')
        return redirect(url_for('localView'))
    return render_template('addrecipe_recipebook.html', title='Add Recipe', form=form)


@app.route('/user/addedrecipes')
@login_required
def localView():
    local_recipes = RecipeLocal.query.filter_by(user_id=current_user.id).all()
    local = []
    for lr in local_recipes:
        local.append({
            'name': lr.recipe_name,
            'ingredients': lr.ing_name,
            'instructions': lr.instructions,
        })
    return render_template('displaylocalrecipe.html', localrecipes=local)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/user/bookmarks')
@login_required
def quickView():
    bookmarked_recipes = current_user.recipes
    bookmarks = []
    for recipe in bookmarked_recipes:
        bookmarks.append({
            'title': recipe.recipe_name,
            'image': recipe.img_url,
            'id': recipe.recipe_id
        })

    return render_template('explore.html', bookmarks=bookmarks)


@app.route('/recipe/<recipe_id>', methods=['GET', 'POST'])
def recipe(recipe_id):
    user = User.query.filter_by(username=current_user.username).first()
    bookmark = False
    planner = False

    if helper_functions.check_if_bookmark_exists(recipe_id, current_user.id):
        bookmark = True
    else:
        bookmark = False
    if helper_functions.check_if_meal_exists_in_planner(recipe_id, current_user.id):
        planner = True
        print(planner)
    else:
        planner = False
        print(False)
    recipe_info_json = api_calls.recipe_info(recipe_id)

    title = recipe_info_json['title']
    img = recipe_info_json['image']
    ingredients = recipe_info_json['extendedIngredients']
    cooking_instructions = recipe_info_json['analyzedInstructions'][0]
    servings = recipe_info_json['servings']
    source = recipe_info_json['sourceName']
    time = 100
    likes = recipe_info_json['aggregateLikes']
    ins = []
    print(cooking_instructions['steps'])
    for element in cooking_instructions['steps']:
        ins.append(
            {
                'step': element['number'],
                'val': element['step']
            })
    if request.method == 'POST':
        if helper_functions.check_if_bookmark_exists(recipe_id, current_user.id):
            bookmark = True
        else:
            bookmark = False
        message = process_recipe_bookmark_button(recipe_id)
        flash(message)
    return render_template("receipe.html", planner=planner, bookmark=bookmark, user=user, title=title, source=source, img=img, ingredients=ingredients, ins=ins, servings=servings, time=time, likes=likes, recipe_id=recipe_id)


@app.route('/planner/<recipe_id>', methods=['GET'])
def meal_planning(recipe_id):
    user = User.query.filter_by(username=current_user.username).first()
    bookmark = False
    planner = False
    if helper_functions.check_if_meal_exists_in_planner(recipe_id, current_user.id):
        planner = True
    else:
        planner = False
    recipe_info_json = api_calls.recipe_info(recipe_id)

    recipe_cals=recipe_info_json['nutrition']['nutrients'][0]["amount"]
    title = recipe_info_json['title']
    img = recipe_info_json['image']
    ingredients = recipe_info_json['extendedIngredients']
    cooking_instructions = recipe_info_json['analyzedInstructions'][0]
    servings = recipe_info_json['servings']

    recipe_cals=recipe_cals/servings

    source = recipe_info_json['sourceName']
    time = 100
    likes = recipe_info_json['aggregateLikes']
    ins = []
    print(cooking_instructions['steps'])
    for element in cooking_instructions['steps']:
        ins.append(
            {
                'step': element['number'],
                'val': element['step']
            })

    bookmark = True 
  
    message = process_meal_planner_button(user.id, recipe_id, recipe_cals)
    flash(message)

    return recipe(recipe_id)


@app.route('/view/details')
def details():
    return render_template('single-post.html')


@app.route('/contact')
def contacts():
    return render_template('contact.html')


@app.route('/category')
def category():
    return render_template('catagory.html')


@app.route('/search')
def recipe_search(result):

    return render_template('catagory-post.html', result=result)


@app.route("/bookmark.json", methods=["POST"])
@login_required
def process_recipe_bookmark_button(recipe_id):
    """Adds bookmark to DB, returning either a success or error message
    back to ajax success function."""

    # Unpack info from ajax

    # Check if recipe in DB. If not, add new recipe to DB.
    current_recipe = helper_functions.check_if_recipe_exists(recipe_id)

    if not current_recipe:
        current_recipe = helper_functions.add_recipe(recipe_id, current_user)

    # Check if user already bookmarked recipe. If not, add to DB.
    bookmark_exists = (helper_functions
                       .check_if_bookmark_exists(recipe_id,
                                                 current_user.id))

    if not bookmark_exists:
        helper_functions.add_bookmark(current_user.id,
                                      recipe_id)
        # Return success message to bookmark-recipe.js ajax success fn
        success_message = "This recipe has been bookmarked!"
        return success_message

    # Return error message to bookmark-recipe.js ajax success fn
    error_message = "You've already bookmarked this recipe."
    return error_message


@login_required
def process_meal_planner_button(user_id, recipe_id, recipe_cals):
    '''
    Function to add a meal to the meal planner similar to bookmarks
    '''
    current_recipe = helper_functions.check_if_recipe_exists(recipe_id)

    if not current_recipe:
        # This is the case if the recipe has been addded into local db or not
        # If the recipe is not present in the db then we cannot add it to planner
        current_recipe = helper_functions.add_recipe(recipe_id, current_user)
        print("Meal not present in db.... \nAdding...")
    helper_functions.add_meal(user_id, recipe_id, recipe_cals)
 
    # Check if the recipe has already been added to planner
    recipe_exists_in_planner = helper_functions.check_if_meal_exists_in_planner(
        recipe_id, user_id)

    if not recipe_exists_in_planner:
        message = "This meal will be added to your Planner."
        try:
            helper_functions.add_meal(recipe_id, current_user.id, recipe_cals)
        except:
            message = "Something went wrong in adding the meal to the Meal Planner"
        finally:
            return message


    day_cals=0          #cals of meals added in a day
    current_user_cals = current_user.cal_req
    planner_recipes = Planner.query.filter_by(user_id=current_user.id).all()

    for recipe in planner_recipes :
        day_cals+=recipe.recipe_cals

    if day_cals>current_user_cals :
        message = "You have exceded your calorific requirements for the day. If you wish to change your meals, visit the Meal Planner."

    elif day_cals==current_user_cals :
        message = "This meal is in your Planner! Your calorie requirements are fulfilled for today."
            
    else :
        message = "This meal is in your Planner"
    return message

@app.route("/profile/",  methods=["GET", "POST"])
@login_required
def view_profile():
    profile = User.query.filter_by(username=current_user.username).first()
    form = RegistrationForm()
    # try:
    # 	if request.method == "POST" and form.validate():
    # 		current_user.weight= form.weight.data
    # 		current_user.height = form.height.data
    # 		current_user.dob = form.dob.data
    # 		current_user.gender = form.gender.data
    # 		db.session.commit()
    # 		return render_template("profile.html", form=form)
    # except:
    #	pass
    if request.method == "GET":
        form.weight.data = current_user.weight
        form.height.data = current_user.height
        form.dob.data = current_user.dob
        form.gender.data = current_user.gender
    return render_template("profile.html", form=form)


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.weight = form.weight.data
        current_user.height = form.height.data
        current_user.dob = form.dob.data
        current_user.gender = form.gender.data
        current_user.exclude = form.exclude.data
        current_user.name = form.name.data
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.set_password(form.password.data)
        current_user.set_age(form.dob.data, form.weight.data, form.height.data,
                             form.gender.data, form.activity_f.data, form.wt_choice.data)
        db.session.commit()
        return redirect(url_for('view_profile'))
    elif request.method == 'GET':
        form.weight.data = current_user.weight
        form.height.data = current_user.height
        form.dob.data = current_user.dob
        form.gender.data = current_user.gender
        form.exclude.data = current_user.exclude
        form.name.data = current_user.name
        form.username.data = current_user.username
        form.email.data = current_user.email
        #form.password.data = current_user.password
    return render_template('edit_profile.html', title='Edit Profile', form=form)

@app.route('/meal_planner', methods=['GET', 'POST'])
@login_required
def meal_planner():
    planner_recipes = Planner.query.filter_by(user_id=current_user.id).all()
    meals = []
    
    current_user_cals = round(current_user.cal_req,2)
    day_cals = 0
    for recipe in planner_recipes:
        recipe_info_json = api_calls.recipe_info(recipe.recipe_id)
        print(recipe.recipe_id)
        print(recipe_info_json)
        day_cals+=recipe.recipe_cals
        meals.append({
            
            'title': recipe_info_json['title'],
            'image': recipe_info_json['image'],
            'servings': recipe_info_json['servings'],
            'id': recipe.recipe_id,
            'cals':recipe.recipe_cals,
            'readyInMinutes' : recipe_info_json['readyInMinutes']
        })

    day_cals=round(day_cals,2)
    
    return render_template('meal_planner.html', title='Meal Planner', meals=meals, current_user_cals=current_user_cals,day_cals=day_cals)


@app.route('/deleteplan/<recipe_id>', methods=['GET'])
def deleteplan(recipe_id):
    
    print(recipe_id)

    del_meal = Planner.query.filter_by(user_id=current_user.id,recipe_id=recipe_id).first()
    db.session.delete(del_meal)
    db.session.commit()
    print(recipe_id)
    message = "Meal deleted from your Planner successfully."
    flash(message)
   
    return redirect(url_for('meal_planner'))



@app.route("/planner.json", methods=["POST"])
@login_required
def process_recipe_planner_button(recipe_id, recipe_cals):
    """Adds meal to DB, returning either a success or error message
    back to ajax success function."""

    # Unpack info from ajax
   
    # Check if recipe in DB. If not, add new recipe to DB.
    current_recipe = helper_functions.check_if_recipe_exists(recipe_id)

    if not current_recipe:
        current_recipe = helper_functions.add_recipe(recipe_id, current_user)

    # Check if user already bookmarked recipe. If not, add to DB.
    meal_exists = (helper_functions
                   .check_if_meal_exists(recipe_id,
                                         current_user))

    if not meal_exists:
        helper_functions.add_meal(current_user.id,
                                  recipe_id, recipe_cals)
        # Return success message to planner-recipe.js ajax success fn
        success_message = "This recipe has been added to the Meal Planner!"
        return success_message

    # Return error message to planner-recipe.js ajax success fn
    error_message = "You've already added this recipe."
    return error_message


@app.route('/list/pantry', methods=['GET', 'POST'])
@login_required
def pantry():
    outlist = PantryList.query.filter_by(user_id=current_user.id).all()
    ings=[]
    for item in outlist:
        ings.append(item.ing_name.upper())

    form1 = PantryForm()
    if form1.add.data:
        listupdate=helper_functions.add_to_pantry(current_user.id, form1.ing_name.data.upper())
        ings.append(form1.ing_name.data.upper())
    
    if form1.delete.data:
        listupdate=helper_functions.delete_from_pantry(current_user.id, form1.ing_name.data.upper())
        ings.remove(form1.ing_name.data.upper())

    if form1.search.data:
        print("searching recipes")
        forsend = PantryList.query.filter_by(user_id=current_user.id).all()
        # send=""
        # send=[]
        # for item in forsend:
        #     send.append(item.ing_name.upper())
        #     # send=send+','+(item.ing_name.upper())
        print("sending")
        # index2(send)
        return render_template('index2.html', title='Results')

    return render_template('pantry2.html', title='Pantry', form=form1, inglist=ings)


@app.route("/user/cals")
@login_required
def get_meals_from_cals():
    current_user_cals = current_user.cal_req
    exclude= current_user.exclude
    response1 = api_calls.recommend_diet_based_on_cals1(current_user_cals, exclude)
    print(response1)
    response2 = api_calls.recommend_diet_based_on_cals2(current_user_cals, exclude)
    print(response2)
    response3 = api_calls.recommend_diet_based_on_cals3(current_user_cals, exclude)
    print(response3)
    current_user_cals = round(current_user.cal_req,2)
    return render_template("recommend.html", recom1=response1["meals"], recom2=response2["meals"], recom3=response3["meals"], current_user_cals=current_user_cals)
