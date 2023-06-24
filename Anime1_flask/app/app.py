from flask import Flask, redirect, render_template, url_for, request
from anime1.explorer import get_menu, get_anime_list
import re
import json

app = Flask(__name__)
info = get_menu()
list_name = get_anime_list()
main_menu = list_name["main_menu"]
sub_menu = list_name["sub_menu"]

def make_row(arg: list):
    name = arg[1]
    r1 = re.findall(r"連載中\(([0-9]+)\)", arg[2]) 
    r2 = re.findall(r"([1-9]+)-([0-9]+)", arg[2])
    
    number = r1[0] if r1 != [] else r2[0][1]
    result = "{}[{}]".format(name, number)

    return result

def make_link(number: int):
    return "http://anime1.me/?cat={}".format(number)

app.jinja_env.globals.update(make_row = make_row, make_link = make_link)

@app.route("/", methods = ["GET", "POST"])
def main():
    if request.method == "POST":
        s2 = request.form.get("search2")
        url = "http://anime1.me/?s={}".format(s2)

        return redirect(url)
    
    return render_template("main.html", info1 = info["content"][: 10], 
                           start = 1, end = 20, total = info["length"], 
                           info = json.dumps(info["content"]),
                            season = main_menu)

@app.route("/<season>")
def season(season: str):
    return render_template("schedule.html", title = main_menu, season = main_menu, month = sub_menu)


if __name__ == '__main__':
    app.run(debug=True)