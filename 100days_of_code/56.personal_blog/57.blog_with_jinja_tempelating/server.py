from flask import Flask, render_template
import requests
from werkzeug.utils import html
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/blog/<num>")
def blog(num):
    response = requests.get("https://api.npoint.io/5c94e6a2fcd1d26bffeb")
    data = response.json()
    return render_template("blog.html", blog_posts=data)

if __name__ == "__main__":
    app.run(debug=True)