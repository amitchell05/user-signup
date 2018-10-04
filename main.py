from flask import Flask, request, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('home_page.html')

def no_spaces(string):
    for char in string:
        if char == " ":
            return False
    return True

def is_empty(string):
    if string == " " or string == "":
        return True
    return False

def valid_len(string):
    if len(string) < 3 or len(string) > 20:
        return False
    return True

def valid_email(string):
    p_count = 0
    at_count = 0

    for char in string:
        if char == ".":
            p_count += 1
        elif char == "@":
            at_count += 1
    
    # works with asdfasdfcom and asdf@asdf and asdf.asdf now, but maybe refactor?
    if not valid_len(string) or not no_spaces(string) or p_count > 1 or at_count > 1 or (p_count == 0 and at_count == 0) or p_count == 0 or at_count == 0:
        return False
    return True

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
    
    if not no_spaces(username) or is_empty(username) or not valid_len(username):
        username_error = "Enter a valid username"

    if not no_spaces(password) or is_empty(password) or not valid_len(password):
        password_error = 'Enter a valid password'
        password = ""

    if not no_spaces(verify) or is_empty(verify) or not valid_len(verify):
        verify = 'Reenter your password'
        verify = ""
    
    if password != verify:
        if not no_spaces(password) or is_empty(password) or not valid_len(password):
            password_error = 'Enter a valid password'
            password = ""
        elif not no_spaces(verify) or is_empty(verify) or not valid_len(verify):
            verify_error = 'Reenter your password'
            verify = ""
        else:
            password_error = 'Passwords do not match'
            verify_error = 'Passwords do not match'
            password = ""
            verify = ""

    if len(email) > 1:
        if not valid_email(email):
            email_error = 'Enter a valid Email'

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