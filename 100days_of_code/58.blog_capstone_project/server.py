from flask import Flask, render_template, request
import requests
import smtplib
app = Flask(__name__)

POST_API = "https://api.npoint.io/0067e63917ca7a5034d9"
response = requests.get(url=POST_API)
blog_posts = response.json()
EMAIL = "spotifyhakk88@gmail.com"
PWD = "00990988"

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


@app.route("/form-entry", methods=["POST"])
def receive_data():
    if request.method == "POST":
        data = request.form
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PWD)
            connection.sendmail(
                from_addr= EMAIL,
                to_addrs= EMAIL,
                msg= f"Subject: HELLO\n\n name: {data['name']}\nemail: {data['email']}\nPhone No: {data['phoneno']}\nMessage: {data['message']}\n"
            )
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


if __name__ == "__main__":
    app.run(debug=True)