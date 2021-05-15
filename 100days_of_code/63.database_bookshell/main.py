from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
# initialize flask app and sqlalchemy database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'
db = SQLAlchemy(app)


# create book table and assign row
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    title = db.Column(db.String(250), unique=True, nullable=False)
    aurthor = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float(), nullable=False)


db.create_all()


@app.route('/')
def home():
    return render_template("index.html", books=Book.query.all())


# insert data into book table
@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        title = request.form['bookname']
        aurthor = request.form['aurthor']
        rating = request.form['rating']
        db.session.add(Book(title=title, aurthor=aurthor, rating=rating))
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")


# get data from url and edit with id in db
@app.route("/edit", methods=['POST', 'GET'])
def edit():
    if request.method == "POST":
        id = request.form["id"]
        rating_edit = request.form["rating_edit"]
        Book.query.get(id).rating = rating_edit
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    return render_template("edit.html", data=Book.query.get(book_id))


# delete file
@app.route("/delete")
def delete():
    id = request.args.get("id")
    db.session.delete(Book.query.get(id))
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
