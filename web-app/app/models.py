from app import db, login
from hashlib import md5
from app import login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime, date
followers = db.Table(
    'followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(120), index=True, unique=True)
    weight = db.Column(db.Float)
    height = db.Column(db.Float)
    dob = db.Column(db.Date)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    bmr = db.Column(db.Float)
    activity_f = db.Column(db.String(5))
    cal_req = db.Column(db.Float)
    exclude = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))
    about_me = db.Column(db.String(140))
    followed = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')

    def __init__(self, **kwargs):
        self.username = kwargs.get('username')
        self.email = kwargs.get('email')
        self.weight = kwargs.get('weight')
        self.height = kwargs.get('height')
        self.dob = kwargs.get('dob')
        self.gender = kwargs.get('gender')
        self.name = kwargs.get('name')
        self.exclude = kwargs.get('exclude')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def set_age(self, dob, weight, height, gender, activity, wt_choice):
        today = date.today()
        self.age = today.year - dob.year - \
            ((today.month, today.day) < (dob.month, dob.day))
        if gender == 'M':
            self.bmr = (10*weight) + (6.25*height) - (5*self.age) + 5
        elif gender == 'F':
            self.bmr = (10*weight) + (6.25*height) - (5*self.age) - 161

        if wt_choice == 'A':
            wt_mlt = 1
        elif wt_choice == 'B':
            wt_mlt = 0.87
        elif wt_choice == 'C':
            wt_mlt = 0.74
        elif wt_choice == 'D':
            wt_mlt = 0.48
        elif wt_choice == 'E':
            wt_mlt = 1.13
        elif wt_choice == 'F':
            wt_mlt = 1.26
        elif wt_choice == 'G':
            wt_mlt = 1.52

        if activity == '1.2':
            self.cal_req = self.bmr * 1.2 * wt_mlt
        elif activity == '1.375':
            self.cal_req = self.bmr * 1.375 * wt_mlt
        elif activity == '1.55':
            self.cal_req = self.bmr * 1.55 * wt_mlt
        elif activity == '1.725':
            self.cal_req = self.bmr * 1.725 * wt_mlt
        elif activity == '1.9':
            self.cal_req = self.bmr * 1.9 * wt_mlt

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)

    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)

    def is_following(self, user):
        return self.followed.filter(
            followers.c.followed_id == user.id).count() > 0

    def followed_recipes(self):
        followed = Recipe.query.join(followers, (followers.c.followed_id == Recipe.user_id)).filter(
            followers.c.follower_id == self.id)
        own = Recipe.query.filter_by(user_id=self.id)
        return followed.union(own)


class RecipeLocal(db.Model):
    __tablename__ = 'recipelocal'
    recipe_id = db.Column(db.Integer, primary_key=True,
                          nullable=False, autoincrement=True)
    recipe_name = db.Column(db.String(200), nullable=True)
    instructions = db.Column(db.String(5000), nullable=True)
    ing_name = db.Column(db.String(64), nullable=True)
    # users = db.relationship("User",secondary="bookmarks",backref=db.backref("recipes"))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, **kwargs):
        self.recipe_name = kwargs.get('recipe_name')
        self.instructions = kwargs.get('instructions')
        self.user_id = kwargs.get('user_id')
        self.ing_name = kwargs.get('ing_name')

    def __repr__(self):
        return """<Recipe recipe_id={} recipe_name={} instructions={} user_id={}  ing_	name={}""".format(self.recipe_id, self.recipe_name,
                                                                                                         self.instructions, self.user_id, self.ing_name)


class Recipe(db.Model):
    __tablename__ = 'recipes'

    recipe_id = db.Column(db.String(64), primary_key=True, nullable=False)
    recipe_name = db.Column(db.String(200), nullable=True)
    img_url = db.Column(db.String(1000), nullable=True)
    instructions = db.Column(db.String(5000), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # Relationships

    cuisines = db.relationship(
        "Cuisine", secondary="recipe_cuisines", backref=db.backref("recipes"))
    users = db.relationship("User", secondary="bookmarks",
                            backref=db.backref("recipes"))

    # def __init__(self,**kwargs):
    # 	self.recipe_name = kwargs.get('recipe_name')
    # 	self.instructions = kwargs.get('instructions')
    # 	self.user_id= kwargs.get('user_id')

    def __repr__(self):
        return """<Recipe recipe_id={} recipe_name={} img_url={}
                  instructions={} user={}>""".format(self.recipe_id, self.recipe_name,
                                                     self.img_url, self.instructions, self.user_id)


class Ingredient(db.Model):
    __tablename__ = 'ingredients'

    ing_id = db.Column(db.String(64), nullable=False, primary_key=True)
    ing_name = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return "<Ingredient ing_id={} ing_name={}>".format(self.ing_id, self.ing_name)


class List(db.Model):
    __tablename__ = 'lists'

    list_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    list_name = db.Column(db.String(60), nullable=True)

    user = db.relationship("User", backref=db.backref("lists"))

    def __repr__(self):
        return "<List list_id={} user_id={} list_name={}>".format(self.list_id, self.user_id, self.list_name)


class Cuisine(db.Model):
    __tablename__ = 'cuisines'

    cuisine_id = db.Column(db.Integer, autoincrement=True,
                           primary_key=True)
    cuisine_name = db.Column(db.String(60), nullable=True)

    def __repr__(self):
        return "<Cuisine cuisine_id={} cuisine_name={}>".format(
            self.cuisine_id, self.cuisine_name)


class RecipeIngredient(db.Model):
    __tablename__ = "recipe_ingredients"
    r_i_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    recipe_id = db.Column(db.String(64), db.ForeignKey('recipes.recipe_id'))
    ing_id = db.Column(db.String(64), db.ForeignKey('ingredients.ing_id'))
    meas_unit = db.Column(db.String(30), nullable=True)
    mass_qty = db.Column(db.Integer, nullable=True)  # NOT to be incremented
    recipe = db.relationship("Recipe", backref="recipe_ingredients")
    ingredient = db.relationship("Ingredient", backref="recipe_ingredients")

    def __repr__(self):
        return """<RecipeIngredient r_i_id={} recipe_id={} ing_id={} meas_unit={} mass_qty={}>""".format(self.r_i_id, self.recipe_id, self.ing_id, self.meas_unit, self.mass_qty)


class ListIngredient(db.Model):
    __tablename__ = "list_ingredients"
    l_i_id = db.Column(db.Integer,
                       autoincrement=True,
                       primary_key=True)
    list_id = db.Column(db.Integer,
                        db.ForeignKey('lists.list_id'))
    ing_id = db.Column(db.String(64), db.ForeignKey('ingredients.ing_id'))
    meas_unit = db.Column(db.String(30), nullable=True)
    mass_qty = db.Column(db.Integer, nullable=True)  # incrementable
    lst = db.relationship("List", backref="list_ingredients")
    ingredient = db.relationship("Ingredient", backref='list_ingredients')

    def __repr__(self):
        return """<ListIngredient l_i_id={} list_id={} ing_id={} meas_unit={} mass_qty={}>""".format(self.l_i_id, self.list_id,
                                                                                                     self.ing_id, self.meas_unit,
                                                                                                     self.mass_qty)


class Bookmark(db.Model):
    __tablename__ = "bookmarks"
    bookmark_id = db.Column(db.Integer,
                            autoincrement=True,
                            primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    recipe_id = db.Column(db.String(64), db.ForeignKey('recipes.recipe_id'))

    def __repr__(self):
        return """<Bookmark bookmark_id={} user_id={} recipe_id={}>""".format(
            self.bookmark_id, self.user_id, self.recipe_id)


class Planner(db.Model):
    __tablename__ = "planner"
    # planner_id = db.Column(db.Integer,
    #                        autoincrement=True,
    #                        primary_key=True)
    # meal_type = db.Column(db.String(64))                       
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    recipe_id = db.Column(db.String(64), db.ForeignKey('recipes.recipe_id'), primary_key=True)
    recipe_cals=db.Column(db.Float)
    # date = db.Column(db.Date)

    def __repr__(self):
        return """<Planner planner_id={} user_id={} recipe_id={} recipe_cals={}>""".format(
             self.user_id, self.recipe_id, self.recipe_cals)


class RecipeCuisine(db.Model):
    __tablename__ = "recipe_cuisines"
    recipe_cuisine_id = db.Column(db.Integer,
                                  autoincrement=True,
                                  primary_key=True)
    cuisine_id = db.Column(db.Integer, db.ForeignKey('cuisines.cuisine_id'))
    recipe_id = db.Column(db.String(64), db.ForeignKey('recipes.recipe_id'))

    def __repr__(self):
        return "<RecipeCuisine recipe_cuisine_id={} cuisine_id={} recipe_id={}>".format(
            self.recipe_cuisine_id, self.cuisine_id, self.recipe_id)


class PantryList(db.Model):
    __tablename__ = "pantry"
    # id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    ing_name = db.Column(db.String(64), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return "<PantryList ing_name={} user_id={}>".format(self.ing_name, self.user_id)
        # return "<PantryList id={} ing_name={} user_id={}>".format(self.id, self.ing_name, self.user_id)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
