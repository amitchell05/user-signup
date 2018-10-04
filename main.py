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
    if not valid_len(string) == True or not no_spaces(string) == True or p_count > 1 or at_count > 1 or (p_count == 0 and at_count == 0) or p_count == 0 or at_count == 0:
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
    
    if no_spaces(username) == False or is_empty(username) == True or valid_len(username) == False:
        username_error = "Enter a valid username"

    if no_spaces(password) == False or is_empty(password) == True or valid_len(password) == False:
        password_error = 'Enter a valid password'
        password = ""

    if no_spaces(verify) == False or is_empty(verify) == True or valid_len(verify) == False:
        verify = 'Reenter your password'
        verify = ""
    
    if password != verify:
        if no_spaces(password) == False or is_empty(password) == True or valid_len(password) == False:
            password_error = 'Enter a valid password'
            password = ""
        elif no_spaces(verify) == False or is_empty(verify) == True or valid_len(verify) == False:
            verify_error = 'Reenter your password'
            verify = ""
        else:
            password_error = 'Passwords do not match'
            verify_error = 'Passwords do not match'
            password = ""
            verify = ""

    if len(email) > 1:
        if valid_email(email) == False:
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