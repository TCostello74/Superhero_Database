from flask import Flask, render_template, redirect, flash, request, session
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, User, Favorite, Hero
from forms import UserForm, SearchForm
import requests

# CURR_USER_KEY = "curr_user"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///superhero-app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "123abc"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


connect_db(app)
db.create_all()

# toolbar = DebugToolbarExtension(app)


@app.route("/")
def home_page():
    return render_template('home.html')


#######################################################################################
"""User register/login"""


@app.route('/register', methods=['GET', 'POST'])
def register_user():
    form = UserForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        new_user = User.register(username, password)

        db.session.add(new_user)
        db.session.commit()
        flash('Welcome! Successfully Created Your Account!')
        return redirect('/')

    return render_template('register.html', form=form)



@app.route('/login', methods=['GET', 'POST'])
def login_user():
    form = UserForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username, password)
        if user:
            return redirect('/search')
        else:
            form.username.errors = ['Invalid username/password!']

    return render_template('login.html', form=form)


#######################################################################################
"""Hero search routes"""


@app.route('/search', methods=['GET', 'POST'])
def search_hero():
    form = SearchForm()
    if form.validate_on_submit():
        hero_name = form.hero_name.data
        return redirect(f'/hero/{hero_name}')

    return render_template('search.html', form=form)



@app.route('/hero/<hero_name>', methods=['GET', 'POST'])
def show_hero(hero_name):
    full_name = request.args.get('full_name')
    token = '2244675209060970'  # Replace with your actual token
    url = f'https://superheroapi.com/api/{token}/search/{hero_name}'
    response = requests.get(url)
    data = response.json()

    if data['response'] == 'success':
        if full_name:
            hero = next((item for item in data['results'] if item['name'].lower() == hero_name.lower() and item['biography']['full-name'].lower() == full_name.lower()), None)
            if hero is None:
                flash('Hero not found!')
                return redirect('/search')
        else:
            matching_heroes = [item for item in data['results'] if item['name'].lower() == hero_name.lower()]
            if len(matching_heroes) == 1:
                hero = matching_heroes[0]
            elif len(matching_heroes) > 1:
                return render_template('select_hero.html', heroes=matching_heroes)
            else:
                flash('Hero not found!')
                return redirect('/search')
    else:
        flash('Hero not found!')
        return redirect('/search')

    return render_template('hero.html', hero=hero)



"""favorites page"""

@app.route('/favorites/add', methods=['POST'])
def add_favorite():
    if 'username' not in session:
        flash('You must be logged in to do that.')
        return redirect('/')
    
    user = User.query.filter_by(username=session['username']).first()
    hero_id = request.form['hero_id']

    # Check if this hero is already a favorite
    if Favorite.query.filter_by(user_id=user.id, hero_id=hero_id).first() is not None:
        flash('This hero is already in your favorites.')
        return redirect(f'/hero/{hero_id}')

    new_favorite = Favorite(user_id=user.id, hero_id=hero_id)
    db.session.add(new_favorite)
    db.session.commit()

    flash('Hero added to favorites!')
    return redirect(f'/hero/{hero_id}')



@app.route('/favorites')
def show_favorites():
    if 'username' not in session:
        flash('You must be logged in to do that.')
        return redirect('/')
    
    user = User.query.filter_by(username=session['username']).first()
    favorites = Favorite.query.filter_by(user_id=user.id).all()

    return render_template('favorites.html', favorites=favorites)













# if __name__ == "__main__":
#     app.run(debug=True)


# token = 2244675209060970