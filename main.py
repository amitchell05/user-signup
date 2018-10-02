from flask import Flask, request, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('home_page.html')

@app.route("/", methods=['POST'])
def welcome():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    
    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""
    
    if " " in username or len(username) < 3 or len(username) > 20:
        username_error = "Enter a valid username"

    if password == "":
        password_error = 'Enter a password'
        password = ""

    if verify == "":
        verify = 'Reenter your password'
        verify = ""
    
    if password != verify:
        if password == "":
            password_error = 'Enter a password'
            password = ""
        elif verify == "":
            verify_error = 'Reenter your password'
            verify = ""
        else:
            password_error = 'Passwords do not match'
            verify_error = 'Passwords do not match'
            password = ""
            verify = ""

    if len(email) > 1:
        if "@" not in email or "." not in email or len(email) < 3 or len(email) > 20:
            email_error = 'Email address invalid'

    if not username_error and not password_error and not verify_error and not email_error:
        return render_template('welcome.html', username=username)
    
    else:
        return render_template('home_page.html',
        username=username,
        username_error=username_error,
        password_error=password_error,
        verify_error=verify_error,
        email=email,
        email_error=email_error) 
        
app.run()