import os
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from forms import AddProjectForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "@Mountaindew24"
Bootstrap(app)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL", "sqlite:///personal_site.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CONFIGURE TABLES
class Projects(db.Model):
    __tablename__ = "projects"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    url = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

# create database
# db.create_all()


@app.route('/')
def home():
    projects = Projects.query.all()
    return render_template("index.html", projects=projects)


@app.route('/add-project', methods=["GET", "POST"])
def add_project():
    form = AddProjectForm()
    if form.validate_on_submit():
        new_project = Projects(
            title=form.title.data,
            description=form.description.data,
            url=form.url.data,
            img_url=form.img_url.data,

        )
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_project.html", form=form)


@app.route("/project/<int:project_id>")
def show_project(project_id):
    requested_project = Projects.query.get(project_id)
    return render_template("project.html", project=requested_project)


if __name__ == "__main__":
    app.run(debug=True)
