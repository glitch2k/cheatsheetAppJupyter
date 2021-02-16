from flask import Flask, render_template, redirect, request
from forms import inputData

app = Flask(__name__)

# this config is used in conjunction with WTFORMS
app.config['SECRET_KEY'] = 'glitch'

# this is a route that tell flask how to get to this page and display it.
# at the browser when [127.0.0.1:5000/] is entered flask will call upon the 
# "home" python function.
# that "home" python function will then do what ever that is in the return section
# of the function.
# in this case it will return the text " search" & "update" with html tags
# search
# update
@app.route("/")
def home():
    return render_template('home.html')

# this route will be used to access the function that will allow the user to enter a new cheatsheet item
# it is called upon by typing the following in the URL bar "127.0.0.1:5000/newitem"
# or it can be called upon but another function by using its function name "newitem"
@app.route("/newitem", methods=['GET', 'POST'])
def newitem():
    form = inputData()
    if form.is_submitted():
        result = request.form
        return render_template('dataFromForms.html', result=result)
    return render_template('input.html', form=form)




if __name__ == "__main__":
    app.run()