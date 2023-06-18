from flask import Flask, redirect, render_template, url_for
from anime1.explorer import explore

app = Flask(__name__)
info = explore()

def make_row(arg: list):
    name = arg[1]
    number = arg[2][3: len(arg[2]) - 1]
    
    result = "{}[{}]".format(name, number)

    return result

def make_link(number: int):
    return "http://anime1.me/?cat={}".format(number)

app.jinja_env.globals.update(make_row = make_row, make_link = make_link)

@app.route("/")
def main():
    return render_template("main.html", info1 = info["content"][: 20], info2 = info["content"][: 10], start = 0, end = 20, total = info["length"])

if __name__ == '__main__':
    app.run(debug=True)