import os
from dotenv import find_dotenv, load_dotenv
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap
import hashlib

load_dotenv(find_dotenv())


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Length(min=9), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
secret_key = hashlib.sha224(os.getenv('secret_key').encode('utf8')).hexdigest()
app.secret_key = secret_key
Bootstrap(app)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["POST", "GET"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "YOUR MAIL" and login_form.password.data == "YOUR PASS":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)