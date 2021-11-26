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
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")