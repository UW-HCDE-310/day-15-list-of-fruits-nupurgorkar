from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def index():
    fruits = [
        {"name": "apples", "quantity": 3},
            {"name": "oranges", "quantity": 2},
            {"name": "strawberries", "quantity": 6}
    ]

    filterf = []
    for fruit in fruits:
        if fruit['name'][0] == 'o' or fruit['quantity'] > 3:
            filterf.append(fruit)

    return render_template("index.html", fruits=fruits)

