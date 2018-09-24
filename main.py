from flask import Flask, request, render_template

form = """

<!doctype html>

<html>

    <body>

        <h1>User Signup</h1>

        <form method="post">

            <label>Username:
                <input name="username" type="text" />
            </label>

            <br>

            <label>Password:
                <input name="password" type="password" />
            </label>

            <br>

            <label>Verify Password:
                <input name="verify" type="password" />
            </label>

            <br>

            <label>Email (optional):
                <input name="email" type="text" />
            </label>

            <br>

            <label>Beginner
                <input type="radio" name="coding_level" value="bg" />
            </label>

            <label>Intermediate
                <input type="radio" name="coding_level" value="in" />
            </label>

            <label>Advanced
                <input type="radio" name="coding_level" value="ad" />
            </label>

            <br>

            <label>Professional Development
                <input type="checkbox" name="coding_goal" value="first-cb" />
            </label>

            <br>

            <label>Personal Hobby
                <input type="checkbox" name="coding_goal" value="second-cb" />
            </label>

            <br>

            <input type="submit" />

        </form>

    </body>

</html>

"""

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def welcome():
    username = request.form['username']
    return '<h1>Welcome, ' + username + '</h1>'

app.run()