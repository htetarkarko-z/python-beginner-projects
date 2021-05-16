from enum import unique
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movie-collection.db"
db = SQLAlchemy(app)
Bootstrap(app)
tmdb_api = "https://api.themoviedb.org/3/search/movie"
api_key = "6cee15315e3fbc8117713de186ab7549"
tmdb_img = "https://image.tmdb.org/t/p/original"


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String, unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String)
    img_url = db.Column(db.String)


class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10")
    review = StringField("Your Review")
    sumit = SubmitField("Done")


class AddMovieForm(FlaskForm):
    title = StringField("Movie Title")
    submit = SubmitField("Add Movie")


db.create_all()


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    db.session.delete(Movie.query.get(movie_id))
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get(
            url=tmdb_api,
            params={"api_key": api_key, "query": movie_title}
            )
        response.raise_for_status()
        data = response.json()["results"]
        return render_template("select.html", options=data)
    return render_template("add.html", form=form)


@app.route("/find_movie")
def find_movie():
    movie_id = request.args.get("id")
    tmdb_search_api = f"https://api.themoviedb.org/3/movie/{movie_id}"
    response = requests.get(url=tmdb_search_api, params={"api_key": api_key})
    data = response.json()
    add_movie = Movie(
        title = data["title"],
        year = data["release_date"],
        description = data["overview"],
        img_url = tmdb_img + data["poster_path"]
    )
    db.session.add(add_movie)
    db.session.commit()
    return redirect(url_for("edit", id=add_movie.id))


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    if movie.rating and movie.review != "":
        form.rating.render_kw = {"placeholder": movie.rating}
        form.review.render_kw = {"placeholder": movie.review}
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)


if __name__ == '__main__':
    app.run(debug=True)
