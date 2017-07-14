#!/usr/bin/env python3

''' 
Github Language Popularity App by Lee Gainer, July 2017
Final project for Harvard cs50
    
This app uses current data from Github accessed via RESTful API
to evaluate the poplarity of various programming languages.
'''

from cs50 import SQL
from flask import Flask, jsonify, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp

from helpers import *

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

# GLOBALS
# Create list of all languages used in Github to pass on to html page
LANGS = ["chapel", "clojure", "coffeescript", "c++", "crystal", "csharp", "css", "factor", "go", "golo",\
"groovy", "gosu", "haxe", "html", "io", "java", "javascript", "julia", "kotlin", "livescript", "nim", "nu",\
"ocaml", "php", "powershell", "purescript", "python", "racket", "red", "ruby", "rust", "swift", "scala",\
"terra", "typescript", "RELOAD"]

@app.route('/', methods = ["GET", "POST"])
def index():
    
    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        
        # Get lang_name value from html buttons on submit
        lang_name = request.form.get("lang_name")
        
        # Correct c++ name for search
        if lang_name == "c++":
            lang_name = "cpp"
            
        # look up language info from GitHub
        r = lookup(lang_name)
        
        # check r for response code
        if r is 2:
            return nope("No" , "404, Not Found")
            
        if r is 3:
            return nope("slow down" , "there's a rate limit ya know")
            
        if r is 4:
            return nope("No" , "Keys")
            
        if r is 5:
            return nope("No" , "Incomplete Results is True")
            
        # if r is 5 or 6:
        #     return nope("Slow down" , "there's an API CALL rate limit ya know")
            
        return render_template("graph.html", LANGS = LANGS)
    
    else:
        indexLangs = LANGS[:-1]
        return render_template("index.html", indexLangs = indexLangs)

@app.route("/graph", methods=["POST"])
def graph():
    
    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        
        # Get lang_name value from html buttons on submit
        lang_name = request.form.get("lang_name")
        
        # Correct c++ name for search
        if lang_name == "c++":
            lang_name = "cpp"
            
        if lang_name == "RELOAD":
            erase_csv()
            indexLangs = LANGS[:-1]
            return render_template("index.html", indexLangs = indexLangs)
            
        # look up language info from GitHub, add data to csv
        r = lookup(lang_name)
        
        # check r for response code
        if r is 2:
            return nope("No" , "404, Not Found")
            
        if r is 3:
            return nope("slow down" , "there's a rate limit ya know")
            
        if r is 4:
            return nope("No" , "Keys")
            
        if r is 5:
            return nope("No" , "Incomplete Results is True")
        
        return render_template("graph.html", LANGS = LANGS)
        
    else:
        return render_template("graph.html", LANGS = LANGS)
        
@app.route("/wrong", methods=["POST"])
def wrong():
    
    check = db.execute("SELECT * FROM githubData")
    
    if check == None:
        return render_template("index.html", LANGS = LANGS)
    else:
        return render_template("graph.html", LANGS = LANGS)
