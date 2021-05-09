from flask import Flask
import random

app = Flask(__name__)

random_num = random.randint(0, 9)
# index route
@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
        "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' />"


@app.route("/<num>")
def user_input(num):
    if int(num) > random_num:
        return "Too High"
    elif int(num) < random_num:
        return "Too Low"
    else:
        return "Correct"


if __name__ == "__main__":
    app.run(debug=True)