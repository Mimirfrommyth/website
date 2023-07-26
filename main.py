from flask import Flask, render_template, request, redirect, url_for
from post import Post
import datetime
from news_api import *

post_objects = []
post_obj1 = Post(article_1_id, article_1_title, article_1_name, article_1_description)
post_obj2 = Post(article_2_id, article_2_title, article_2_name, article_2_description)
post_obj3 = Post(article_3_id, article_3_title, article_3_name, article_3_description)
post_obj4 = Post(article_4_id, article_4_title, article_4_name, article_4_description)
post_obj5 = Post(article_5_id, article_5_title, article_5_name, article_5_description)
post_obj6 = Post(article_6_id, article_6_title, article_6_name, article_6_description)
post_obj7 = Post(article_7_id, article_7_title, article_7_name, article_7_description)
post_obj8 = Post(article_8_id, article_8_title, article_8_name, article_8_description)
post_obj9 = Post(article_9_id, article_9_title, article_9_name, article_9_description)
post_obj10 = Post(article_10_id, article_10_title, article_10_name, article_10_description)
post_objects.append(post_obj1)
post_objects.append(post_obj2)
post_objects.append(post_obj3)
post_objects.append(post_obj4)
post_objects.append(post_obj5)
post_objects.append(post_obj6)
post_objects.append(post_obj7)
post_objects.append(post_obj8)
post_objects.append(post_obj9)
post_objects.append(post_obj10)

current_year = datetime.datetime.now().year

app = Flask(__name__)

@app.route("/home")
def home():
    if not current_user.is_authenticated:
        return app.login_manager.unauthorized()
    return render_template("home.html", all_posts=post_objects, year=current_year, logged_in=current_user.is_authenticated)

@app.route("/about")
def about():
    if not current_user.is_authenticated:
        return app.login_manager.unauthorized()
    return render_template("about.html", logged_in=current_user.is_authenticated)

@app.route("/contact", methods=['POST','GET'])
def contact():
    if not current_user.is_authenticated:
        return app.login_manager.unauthorized()
    return render_template("contact.html", logged_in=current_user.is_authenticated)

@app.route("/contact/submit", methods=['POST','GET'])
def submit_form():
    ans = "y"
    while True:
        return "Form Submitted Successfully"
    return redirect(url_for(home))
#==================================================================================================================
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

login_manager = LoginManager()
login_manager.init_app(app)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB.
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()

        # Check stored password hash against entered password hashed.
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
            # Password incorrect
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
            # Email exists and password correct
        else:
            login_user(user)
            return redirect(url_for('home'))
    return render_template("login.html", logged_in=current_user.is_authenticated)

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':

        if User.query.filter_by(email=request.form.get('email')).first():
            # User already exists
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))

        hash_and_salted_password = generate_password_hash(
            request.form.get('password'),
            method='pbkdf2:sha256',
            salt_length=8)
        new_user = User(
            email = request.form.get('email'),
            password = hash_and_salted_password,
            name = request.form.get('name')
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for("home"))
    return render_template("register.html")

@app.route("/logout", methods=['GET','POST'])
def logout():
    return render_template("logout.html")

#=================================================================================================
if __name__ == "__main__":
    app.run(debug=True)