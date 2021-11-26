from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    return render_template("tasks.html")

# navbar reffers to the name of the junction not the @app.route("/categories")

@app.route("/categories")
def categories():
    return render_template("categories.html")

# need to include methods here
# get is to get the page
# post is to post data to database

@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        # post method will create new variable category that is set to 
        # new instance of Category model (the table header from the models.py)
        # name attribute in the form needs to match database model

        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        # after the data is submitted to the database, we are redirecting
        # the user back to categories.html page
        return redirect(url_for("categories"))

    # default method is get - so this will return "add_category.html" unless the method is POST
    # it is good practice to add error handling and defence programing here
    return render_template("add_category.html")