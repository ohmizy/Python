from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<int:num>/<color>')
@app.route('/<int:num>')
def hello_world(num, color='blue'):
  title = "Welcome!"
  return render_template("index.html", title_from_backend=title, num=num, color=color)
def route():
  return "Welcome!"

@app.route('/say/<play>')
def say(play):
  return f"hello{play}"

@app.route('/repeat/<int:num>/<pineapple>')
def say1(num,pineapple):
  return f"hello{pineapple * num}"


if __name__=="__main__":
    app.run(debug=True)