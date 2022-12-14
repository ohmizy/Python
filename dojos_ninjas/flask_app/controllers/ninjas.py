from flask_app import app, render_template, request, redirect
from flask_app.models.ninja import Ninja

# ! CREATE
@app.route("/create/ninja", methods = ["post"])
def create_ninja():
  print(request.form)
  Ninja.save(request.form)
  return redirect("/")

# ! READ ALL
@app.route("/ninjas")
def ninjas():
  return render_template("index.html", ninjas=Ninja.get_all())

# ! READ ONE
@app.route ("/show/ninja/<int:id>")
def show_ninja(id):
  data = {"id":id}
  ninja = Ninja.get_one(data)
  return render_template("show_ninja.html", ninja = ninja)

# ! UPDATE
@app.route("/edit/<int:id>")
def edit_ninja(id):
  data = {"id":id}
  return render_template("edit_ninja.html", ninja = Ninja.get_one(data))

@app.route("/update/ninja", methods = ["post"])
def update_ninja():
  print(request.form)
  Ninja.update(request.form)
  return redirect("/")

# ! DELETE
@app.route("/delete/<int:id>")
def delete_ninja(id):
  Ninja.destroy({"id":id})
  return redirect("/")