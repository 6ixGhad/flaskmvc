from flask import Blueprint, redirect, render_template, request
#from forms import SignUp, LogIn, AddTodo

api_views = Blueprint('api_views', __name__, template_folder='../templates')

@api_views.route('/status', methods=['GET'])
def get_api_docs():
    return render_template('index.html')

@api_views.route('/', methods=['GET'])
def index():
    return render_template('login.html')


@api_views.route('/signup', methods=['GET'])
def signup():
  form = SignUp() # create form object
  return render_template('signup.html', form=form) # pass form object to template

'''
How to signup with server side rendering
0. assume html form submission with POST method
1. create a post route
2. take data from form
3. check if form is valid
4. if form is invalid flash error message and redirect user
5. else get data from form
6. create model object from data
7. save object to db
8. flash success message
9. redirect user
'''
@api_views.route('/signup', methods=['POST'])
def signupAction():
  form = SignUp() # create form object
  if form.validate_on_submit():
    data = request.form # get data from form submission
    newuser = User(username=data['username'], email=data['email']) # create user object
    newuser.set_password(data['password']) # set password
    db.session.add(newuser) # save new user
    db.session.commit()
    flash('Account Created!')# send message
    return redirect(url_for('index'))# redirect to login page
  flash('Error invalid input!')
  return redirect(url_for('signup')) 