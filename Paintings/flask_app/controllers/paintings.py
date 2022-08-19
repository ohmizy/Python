from flask_app import app, render_template, request, redirect, session
from flask_app.models.painting import Painting
from flask_app.models.user import User

@app.route("/new/painting")
def new_painting():

  return render_template("new_painting.html")

# ! CREATE
@app.route("/create/painting", methods = ["post"])
def create_painting():
  print(request.form)
  if not Painting.validate_painting(request.form):
    return redirect ("/new/painting")
  painting = Painting.save(request.form)
  return redirect("/paintings")

# ! READ ALL
@app.route("/dashboard")
@app.route("/paintings")
def paintings():
  if "user_id" not in session:
    return redirect ("/logout")
  return render_template("dashboard.html", paintings=Painting.get_all_with_user())

# ! READ ONE
@app.route ("/show/painting/<int:id>")
def show_painting(id):
  data = {"id":id}
  painting = Painting.get_one(data)
  user = User.get_one({'id':painting.user_id})
  return render_template("show_painting.html", painting = painting)

# ! UPDATE
@app.route("/edit/<int:id>")
def edit_painting(id):
  data = {"id":id}
  return render_template("edit_painting.html", painting = Painting.get_one(data))

@app.route("/update/painting", methods = ["post"])
def update_painting():
  print(request.form)
  if "user_id" not in session:
    return redirect ("/logout")
  print(request.form)
  Painting.update(request.form)
  return redirect("/dashboard")

# ! DELETE
@app.route("/delete/<int:id>")
def delete_painting(id):
  Painting.destroy({"id":id})
  return redirect("/dashboard")