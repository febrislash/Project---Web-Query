from logging import exception
from os import abort
from flask import Flask, render_template, request, redirect, abort, jsonify, send_from_directory, url_for
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/static/<filename>")
def statics(filename):
    return send_from_directory('static', filename)

@app.route('/item/new')
def new_item():
    return render_template('new_item.html')


if __name__ == '__main__':
    app.run(debug=True)