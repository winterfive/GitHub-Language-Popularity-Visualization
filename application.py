#!/usr/bin/env python3

from cs50 import SQL
from flask import Flask, jsonify, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp

from helpers import*

# configure application
app = Flask(__name__)

# ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# configure CS50 Library to use SQLite database
db = SQL("sqlite:///languages.db")

# GLOBALS
# Create list of all languages used in Github to pass on to html page
LANGS = ["chapel", "clojure", "coffeescript", "c++", "crystal", "csharp", "css", "factor", "flask", "go", "golo",\
"groovy", "gosu", "haxe", "html", "io", "java", "javascript", "julia", "kotlin", "livescript", "nim", "nu",\
"ocaml", "php", "powershell", "purescript", "python", "racket", "red", "ruby", "rust", "swift", "scala",\
"terra", "typescript"]


@app.route("/", methods = ["GET", "POST"])
def index():
    
    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        
        # Get lang_name value from html buttons on submit
        lang_name = request.form.get('lang_name')
        
        # Correct c++ name for search
        if lang_name == 'c++':
            lang_name = 'cpp'
            
        # look up language info from GitHub
        r = lookup(lang_name)
        
        if r == None:
            return nope("Something","is wrong")
            
        # Change C++ back for use in graph
        if lang_name == 'cpp':
            lang_name = 'c++'
            
        # add data to table
        '''TODO'''
         
        # render stars.html with language name & stars info
        return render_template("graph.html", LANGS = LANGS)
        
   # else if user reached route via GET (as by clicking a link or via redirect)

    else:
        # display index page w/ paragraph
        return render_template("index.html")

@app.route('/graph')
def graph():
    '''TODO'''
    
    # if, check that table has data, if not, display index
    
    # else, get data from table, display on graph
