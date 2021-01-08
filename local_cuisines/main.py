import projects #projects definitions are placed in different file
import data

# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template
#create a Flask instance
app = Flask(__name__)

#connects default URL of server to render home.html
@app.route('/')
def home_route():
    return render_template("travel.html", projects=projects.setup())


@app.route("/sandiego/")
def sandiego_route():
    return render_template("sandiego.html", projects=projects.setup())

@app.route("/losangeles/")
def losangeles_route():
    return render_template("losangeles.html", projects=projects.setup())

@app.route("/sanfrancisco/")
def sanfrancisco_route():
    return render_template("sanfrancisco.html", projects=projects.setup())

@app.route("/search/")
def search_route():
    return render_template("search.html", projects=projects.setup())




if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True)
