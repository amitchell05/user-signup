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

    if username == "":
        username_error = 'Enter a username'
        #return render_template('home_page.html', username=username, username_error=username_error)
    
    if " " in username:
        username_error = "Username invalid"
    
    if len(username) < 3 or len(username) > 20:
        username_error = "Username invalid"

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

    if email != "":
        email = email
    
    if " " in email:
        email_error = 'Email address invalid'
        #return render_template('home_page.html', email=email, email_error=email_error)
    
    if "@" not in email and "." not in email:
        email_error = 'Email address invalid'
        #return render_template('home_page.html', email=email, email_error=email_error)

    if len(email) < 3 or len(email) < 20:
        email_error = 'Email address invalid'
        #return render_template('home_page.html', email=email, email_error=email_error)
        
    #TODO add validation for email that detects '@' and ".com, .org", etc.
    
    if not username_error and not password_error and not verify_error or not email_error:
        return render_template('welcome.html', name=username)
    
    else:
        return render_template('home_page.html',
        username_error=username_error, 
        password_error=password_error,
        verify_error=verify_error,
        email_error=email_error)
        
app.run()