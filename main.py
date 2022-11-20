from flask import Flask, render_template, request, redirect, url_for, session
import firebase_admin
import pyrebase
from firebase_admin import credentials, firestore
import joblib
import pandas as pd
days_of_the_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
today_and_next_day = [20, 21, 22, 23, 24, 25, 19]
cred = {
    'Removed for security reasons', 'Removed for security reasons',
}
firebase = pyrebase.initialize_app(cred)
auth = firebase.auth()
app = Flask(__name__)
app.secret_key = 'secret'
user = None
error_msg = None
@app.route('/login-user', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            session['user'] = user
            return redirect(url_for('home'))
        except:
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/signup')
def signup():
    if user is not None:
        return redirect(url_for('home'))
    return render_template('signup.html')


@app.route('/add-user', methods=['GET', 'POST'])
def add_user():
    email = request.form['email']
    password = request.form['password']
    user = auth.create_user_with_email_and_password(email, password)
    session['user'] = user
    print(session)
    return redirect(url_for('home'))
@app.route('/login')
def login():
    if 'user' in session:
        return redirect(url_for('home'))
    else:
        return render_template('login.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    if 'user' in session:
        user = session['user']
        email = user['email']
        if 'results' in session:
            results = session['results']
            print(results)
            return render_template('dashboard.html', email=email, results=results, days_of_the_week=days_of_the_week, today_and_next_day=today_and_next_day)
        return render_template('dashboard.html', user=user, email=email, results = [])
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    session.pop('results', None)
    return redirect(url_for('index'))

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        age = int(request.form['age'])
        weight = int(request.form['weight'])
        calories_want = int(request.form['calories_want'])
        height = int(request.form['height'])
        df = pd.read_csv("datasets/exercise_dataset.csv")
        if weight < 140:
            loaded_model = joblib.load('130weightModel.sav')
        elif weight < 170:
            loaded_model = joblib.load('155weightModel.sav')
        elif weight < 200:
            loaded_model = joblib.load('180weightModel.sav')
        else:
            loaded_model = joblib.load('205weightModel.sav')
        results = [age, weight, height, calories_want]
        for j in range(6):
            result = round(loaded_model.predict([calories_want]))
            with open("datasets/exercise_dataset.csv", 'r') as f:
                for (i, line) in enumerate(range(result+1)):
                    dfline = f.readline(line)
                    if i == result:
                        exercise = dfline.split(",")[0]
                        exercise_detail = dfline.split(",")[1]
                        try:                       
                            if exercise_detail[0] == "4" or exercise_detail[0] == "5" or exercise_detail[0] == "6" or exercise_detail[0] == "7" or exercise_detail[0] == "8" or exercise_detail[0] == "9" or exercise_detail[0] == "0" or exercise_detail[0] == "1" or exercise_detail[0] == "2" or exercise_detail[0] == "3":
                                exercise_detail = "No specifics for this, just repeatedly use it"
                        except:
                            pass
                        if 'user' in session:
                            user = session['user']
                            email = user['email']
                            print(j)
                            if (exercise[0] == '"'):
                                exercise = exercise[1:]
                            if (exercise[-1] == '"'):
                                exercise = exercise[:-1]
                            if (exercise_detail[0] == '"'):
                                exercise_detail = exercise_detail[1:]
                            if (exercise_detail[-1] == '"'):
                                exercise_detail = exercise_detail[:-1]
                            else:
                                pass
                            results.append([exercise, exercise_detail, days_of_the_week[j], today_and_next_day[j]])
            calories_want -= 100
        session['results'] = results
    return redirect(url_for('home'))
@app.route('/map')
def map():
    if 'user' in session:
        user = session['user']
        email = user['email']
        return render_template('fitness.html', email=email)
    else:
        return redirect(url_for('login'))
app.run(host='0.0.0.0', port=81, debug=True)
