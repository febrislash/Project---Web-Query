from logging import exception
from os import abort
from flask import Flask, render_template, request, redirect, abort, jsonify, send_from_directory, url_for, g
from flask_mysqldb import MySQL
import sqlite3
#import yaml

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/static/<filename>")
def statics(filename):
    return send_from_directory('static', filename)

@app.route('/item/new', methods=["GET", "POST"])
def new_item():
    conn = get_db()
    c = conn.cursor()

    if request.method == "POST":
        # process data jika post
        c.execute("""INSERT INTO items
                    (title, description, price, image, category_id, subcategory_id)
                    VALUES(?,?,?,?,?,?)""",
                    (
                        request.form.get("title"),
                        request.form.get("description"),
                        float(request.form.get("price")),
                        "",
                        1,
                        1    
                    )
                )
        conn.commit()
        return redirect(url_for("home"))
    return render_template('new_item.html')

def get_db():
    db = getattr(g, "_database", None)
    if db is None:
       db =  g._database = sqlite3.connect("db/globomantics.db")
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run(debug=True)