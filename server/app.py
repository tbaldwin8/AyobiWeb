####### IMPORTS #########
import os
import secrets
import PIL
from PIL import Image
from flask import Flask, render_template, request, redirect, url_for, flash, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, current_user, logout_user, login_required
from datetime import datetime
from flask_wtf import FlaskForm 
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

####### CONFIGURATION #########
app = Flask(__name__, static_folder="../static",
	template_folder="../static")

app.config['SECRET_KEY'] = 'ecaf1e9644f3e53c6bfe13704717c3a0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/toddbaldwin/Documents/AyobiFiles/AyobiWeb/server/users.db' 
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

from manage import db, app

####### DATABASE MODELS #########
class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)
	first_name = db.Column(db.String(120), nullable=False)
	last_name = db.Column(db.String(120), nullable=False)
	age = db.Column(db.Integer, nullable=False)
	gender = db.Column(db.String(20), nullable=False)
	image_file = db.Column(db.String(20), unique=True, nullable=False, default='defaultaccount.jpg')
	bio = db.Column(db.Text)
	posts = db.relationship('Fitpost', backref='author', lazy=True)

	def __repr__(self):
		return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Fitpost(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	weight = db.Column(db.Integer)
	bodyfat = db.Column(db.Integer)
	rhr = db.Column(db.Integer)
	prog_pic = db.Column(db.String(20), default='defaultaccount.jpg')
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	note = db.Column(db.Text)
	workout = db.Column(db.Text)
	public = db.Column(db.Boolean, default=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __repr__(self):
		return f"Fitpost('{self.date_posted}')"	


####### FORMS #########
class RegistrationForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	first_name = StringField('First Name', validators=[DataRequired(), Length(min=1, max=120)])
	last_name = StringField('Last Name', validators=[DataRequired(), Length(min=1, max=120)])
	age = IntegerField('Age', validators=[DataRequired()])
	gender = StringField('Gender', validators=[DataRequired()])
	image_file = FileField('Upload Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
	bio = TextAreaField('Bio')
	submit = SubmitField('Sign Up')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('That username is taken. Please choose a different username.')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('That email is taken. Please choose a different email.')

class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
	first_name = StringField('First Name', validators=[DataRequired(), Length(min=1, max=120)])
	last_name = StringField('Last Name', validators=[DataRequired(), Length(min=1, max=120)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
	bio = TextAreaField('Bio')
	submit = SubmitField('Update')

	def validate_username(self, username):
		if username.data != current_user.username:
			user = User.query.filter_by(username=username.data).first()
			if user:
				raise ValidationError('That username is taken. Please choose a different username.')

	def validate_email(self, email):
		if email.data != current_user.email:
			user = User.query.filter_by(email=email.data).first()
			if user:
				raise ValidationError('That email is taken. Please choose a different email.')

class FitpostForm(FlaskForm):
	weight = IntegerField('Weight (lbs)')
	bodyfat = IntegerField('Body Fat Percentage (%)')
	rhr = IntegerField('Resting Heart Rate (bpm)')
	note = TextAreaField('Tell us about your fitness journey since your last post!')
	workout = TextAreaField('Describe your workout routine since your last post.')
	prog_pic = FileField('Upload Progress Picture', validators=[FileAllowed(['jpg', 'png'])])
	public = BooleanField('Make Public')
	submit = SubmitField('Post')

class UpdateFitpostForm(FlaskForm):
	weight = IntegerField('Weight (lbs)')
	bodyfat = IntegerField('Body Fat Percentage (%)')
	rhr = IntegerField('Resting Heart Rate (bpm)')
	note = TextAreaField('Tell us about your fitness journey since your last post!')
	workout = TextAreaField('Describe your workout routine since your last post.')
	prog_pic = FileField('Update Progress Picture', validators=[FileAllowed(['jpg', 'png'])])
	public = BooleanField('Make Public')
	submit = SubmitField('Update')

		
####### METHODS #########
def save_prog_picture(form_picture):
	random_hex = secrets.token_hex(8)
	_, f_ext = os.path.splitext(form_picture.filename)
	picture_fn = random_hex + f_ext
	picture_path = os.path.join(app.root_path, '../static/images/prog_pics', picture_fn)
	
	output_size = (1000, 1000)
	#i = Image.open(form_picture)
	#i.thumbnail(output_size)
	#i.save(picture_path)
	i = Image.open(form_picture)
	cropped_top = i.height/10
	cropped_bottom = i.height - (i.height/10)
	cropped_img = i.crop((0, cropped_top, i.width, cropped_bottom ))
	cropped_img.thumbnail(output_size, Image.ANTIALIAS)
	cropped_img.save(picture_path)

	return picture_fn

def save_prof_picture(form_picture):
	random_hex = secrets.token_hex(8)
	_, f_ext = os.path.splitext(form_picture.filename)
	picture_fn = random_hex + f_ext
	picture_path = os.path.join(app.root_path, '../static/images/prof_pics', picture_fn)
	
	#output_size = (125, 125)
	#i = Image.open(form_picture)
	#i.thumbnail(output_size)
	#i.save(picture_path)

	output_size = (400, 400)
	i = Image.open(form_picture)
	cropped_left = i.width/10
	cropped_right = i.width - cropped_left 
	cropped_top = i.height/10
	cropped_bottom = i.height - ((i.height * 3)/10)
	cropped_img = i.crop((cropped_left, cropped_top, cropped_right, cropped_bottom ))
	cropped_img.thumbnail(output_size, Image.ANTIALIAS)
	cropped_img.save(picture_path)
	return picture_fn
####### ROUTES #########

@app.route("/")
@app.route("/home")
def home():
	posts = Fitpost.query.filter_by(public=True).order_by(Fitpost.date_posted.desc()).all()

	return render_template("home.html", posts=posts)

@app.route("/register", methods=['POST', 'GET'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = RegistrationForm()
	if form.validate_on_submit():
		if form.image_file.data:
			picture_file = save_prof_picture(form.image_file.data)
		hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data, first_name=form.first_name.data, last_name=form.last_name.data, 
			email=form.email.data, age=form.age.data, gender=form.gender.data, bio=form.bio.data, image_file=picture_file, password=hashed_pw)
		db.session.add(user)
		db.session.commit()
		flash('An account has been created for %s! You are now able to log in.' % form.username.data, 'success')
		return redirect(url_for('login'))
	return render_template("register.html", title='Register', form=form)

@app.route("/login", methods=['POST', 'GET'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			return redirect(url_for('home'))
		else:
			flash('Login Unsuccessful. Please check email and password', 'danger')
	return render_template("login.html", title='Login', form=form)

@app.route("/logout", methods=['POST', 'GET'])
def logout():
	logout_user()
	return redirect(url_for('home'))

@app.route('/post/<int:post_id>')
def post(post_id):
	post = Fitpost.query.get_or_404(post_id)
	image_file = url_for('static', filename='images/prof_pics/' + post.author.image_file)
	return render_template('post.html', post=post, image_file=image_file)

@app.route('/post/<int:post_id>/update', methods=['POST', 'GET'])
@login_required
def update_post(post_id):
	post = Fitpost.query.get_or_404(post_id)
	if post.author != current_user:
		abort(403)
	form = UpdateFitpostForm()
	if form.validate_on_submit():
		if form.prog_pic.data:
			picture_file = save_prog_picture(form.prog_pic.data)
			post.prog_pic = picture_file
		post.weight = form.weight.data
		post.bodyfat = form.bodyfat.data
		post.rhr = form.rhr.data
		post.note = form.note.data
		post.workout = form.workout.data
		post.public = form.public.data
		db.session.commit()
		flash('Your post has been updated!', 'success')
		return redirect(url_for('post', post_id=post.id))
	elif request.method == 'GET':
		form.weight.data = post.weight
		form.bodyfat.data = post.bodyfat
		form.rhr.data = post.rhr
		form.note.data = post.note
		form.workout.data = post.workout
		form.public.data = post.public
	return render_template('updatepost.html', form=form)

@app.route('/add')
def add():
	return render_template('add.html')

@app.route('/addpost', methods=['POST', 'GET'])
@login_required
def addpost():
	form = FitpostForm()
	if form.validate_on_submit():
		if form.prog_pic.data:
			picture_file = save_prog_picture(form.prog_pic.data)
		post = Fitpost(weight=form.weight.data, bodyfat=form.bodyfat.data, rhr=form.rhr.data, 
			prog_pic=picture_file, date_posted=datetime.now(), user_id=current_user.id, 
			note=form.note.data, workout=form.workout.data, public=form.public.data)
		db.session.add(post)
		db.session.commit()
		flash('Your post has been created!', 'success')
		return redirect( url_for('home'))
	return render_template('add.html', form=form)

@app.route('/myposts')
@login_required
def my_posts():
	posts = Fitpost.query.filter_by(user_id= current_user.id).order_by(Fitpost.date_posted.desc()).all()
	image_file = url_for('static', filename='images/prof_pics/' + current_user.image_file)
	return render_template('my_posts.html', posts=posts, image_file=image_file)

@app.route("/account", methods=['POST', 'GET'])
@login_required
def account():
	form = UpdateAccountForm()
	if form.validate_on_submit():
		if form.picture.data:
			picture_file = save_prof_picture(form.picture.data)
			current_user.image_file = picture_file
		current_user.username = form.username.data
		current_user.email = form.email.data
		current_user.first_name = form.first_name.data
		current_user.last_name = form.last_name.data
		current_user.bio = form.bio.data
		db.session.commit()
		flash('Your account has been updated!', 'success')
		return redirect(url_for('account'))
	elif request.method == 'GET':
		form.username.data = current_user.username
		form.email.data = current_user.email
		form.first_name.data = current_user.first_name
		form.last_name.data = current_user.last_name
		form.bio.data = current_user.bio
	image_file = url_for('static', filename='images/prof_pics/' + current_user.image_file)
	return render_template('account.html', title='Account', image_file=image_file, form=form)

####### RUNS APPLICATION #########
if __name__=="__main__":
	app.run(debug=True)