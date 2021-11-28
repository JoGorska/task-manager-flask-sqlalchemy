from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    tasks = list(Task.query.order_by(Task.category_id).all())
    return render_template("tasks.html", tasks=tasks)

@app.route("/edit_task/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    if request.method == "POST":
        task.task_name = request.form.get("task_name")
        db.session.commit()
        return redirect(url_for("tasks"))
    return render_template("edit_task.html", task=task)

# navbar reffers to the name of the junction not the @app.route("/categories")

@app.route("/categories")
def categories():
    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories)

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

    # default method is get - so this will return "add_category.html" unless
    #  the method is POST
    # it is good practice to add error handling and defence programing here
    return render_template("add_category.html")


@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)
    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category)

@app.route("/delete_category/<int:category_id>")
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for("categories"))

# Tasks - adding, viewing, editing, deleting

@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    # user needs to choose a category before adding a task, this gets all existing categories from the database
    categories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        task = Task(
            task_name=request.form.get("task_name"),
            task_description=request.form.get("task_description"),
            is_urgent=bool(True if request.form.get("is_urgent") else False),
            due_date=request.form.get("due_date"),
            category_id=request.form.get("category_id")
        )
 
        db.session.add(task)
        db.session.commit()

        return redirect(url_for("home"))

    return render_template("add_task.html", categories=categories)

