#file web.py

#import Flask and render_template to use HTML files
from flask import Flask, render_template, request, jsonify, redirect, make_response, url_for, session

#kee[ track of time for session logout
from datetime import timedelta

#import database and be able to add messages
from database import add_message, get_all_messages, register_user, verify_user


#initialize the Flask app
app = Flask(__name__)
app.secret_key = 'your_random_secret_key' #required for securing sessions 
app.permanent_session_lifetime = timedelta(minutes=5) #sess expire after 5 min

#define the route for the homepage (root URL)
@app.route('/')
def home():
    #look for 'index.html' inside the templates
    return render_template('index.html')

#define the route for the resume page
@app.route('/resume')
def resume():
    return render_template('resume.html')

#define the route for the about page
@app.route('/about')
def about():
    return render_template('about.html')

#define the route for the contact page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        #get json data sent from javascript
        data= request.get_json()

        #extract + validate form fields
        name = data.get('name', '').strip()
        email= data.get('email', '').strip()
        message=data.get('message', '').strip()

        #server-side validation
        if not name or not email or not message:
            return jsonify({'status': 'error', 'message': 'All fields are required'}),400
        if len(name) < 2:
            return jsonify({'status': 'error', 'message': 'Name must be at least 2 characters'}), 400
        if len(message) < 10:
            return jsonify({'status': 'error', 'message': 'Message must be at least 10 characters'}), 400

        #save to database
        add_message(name, email, message)

        #return success response as json
        return jsonify({'status': 'success', 'message': 'Thank you! Your message has been received.'})

    #for GET request, show contact page normally
    return render_template('contact.html')

#route to registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username').strip()
        password = request.form.get('password').strip()

        if username and password:
            success = register_user(username, password)
            if success:
                return redirect('/login')
            else:
                return render_template('register.html', error='Username already exists.')

        return render_template('register.html', error='Please fill out all fields.')

    return render_template('register.html')

#define route message page
@app.route('/messages')
def messages():
    if 'username' not in session:
        return redirect('/login')

    username = session['username']
    all_messages = get_all_messages()
    return render_template('messages.html', messages=all_messages, username=username)

#def route to  login page/ set cookies
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username').strip()
        password = request.form.get('password').strip()

        if verify_user(username, password):
            session.permanent = True
            session['username'] = username
            resp = make_response(redirect('/messages'))
            resp.set_cookie('user_password', password, max_age=3600)  #stores password in cookie (for project requirement)
            return resp
        else:
            return render_template('login.html', error='Invalid username or password.')

    return render_template('login.html')


#define route to logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    resp= make_response(redirect('/login'))
    resp.set_cookie('user_password', '', expires=0)
    return resp

#this runs the app when you type: python app.py
if __name__ == '__main__':
    #debug=True helps automatically reload when you change files
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5055, debug=True)


