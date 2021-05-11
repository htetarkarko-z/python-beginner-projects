from flask import Flask, render_template
import requests
app = Flask(__name__)

POST_API = "https://api.npoint.io/0067e63917ca7a5034d9"
response = requests.get(url=POST_API)
blog_posts = response.json()


@app.route("/")
def index():
    return render_template("index.html", blog_posts=blog_posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<post_id>")
def post(post_id):
    return render_template("post.html", post_id=int(post_id), blog_posts=blog_posts)


if __name__ == "__main__":
    app.run(debug=True)