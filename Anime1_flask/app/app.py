from flask import Flask, redirect, render_template, url_for
from anime1.explorer import explore

app = Flask(__name__)
info = explore()

@app.route("/")
def main():
    return render_template("main.html", info = info["content"][: 20], start = 0, end = 20, total = info["length"])

if __name__ == '__main__':
    app.run(debug=True)