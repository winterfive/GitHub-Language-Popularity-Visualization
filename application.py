#!/usr/bin/env python3

import os
import re
import json
from flask import Flask, jsonify, render_template, request, url_for
from flask_jsglue import JSGlue
import requests
#import csv

from helpers import *

# configure application
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    # Create list of all languages used in Github to pass on to html page
    langs = ["chapel", "clojure", "coffeescript", "c++", "crystal", "csharp", "css", "factor", "flask", "go", "golo",\
        "groovy", "gosu", "haxe", "html", "io", "java", "javascript", "julia", "kotlin", "livescript", "nim", "nu",\
        "ocaml", "php", "powershell", "purescript", "python", "racket", "red", "ruby", "rust", "swift", "scala",\
        "terra", "typescript"]
    
    # render index.html with language name info
    return render_template("index.html", langs = langs)
    
    # Get lang_name value from html buttons
    lang_name = request.form.get('lang_name')
    
    # Correct c++ name for search
    if lang_name == 'c++':
        lang_name = 'cpp'
        
    # look up language info from GitHub
    r = lookup(lang_name)
    
    # Change C++ back for use in graph
    if lang_name == 'cpp':
        lang_name = 'c++'
     
    # render stars.html with language name & stars info
    return render_template("stars.html", lang_name = lang_name, total_stars = r)   
    
    # # Store language name and stars data in new csv file
    # # If csv already exists, append it
    # if os.path.exists('data.csv'):
    #     with open('data.csv', 'a', newline='') as csvfile:
    #         filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #         filewriter.writerow([current_lang, total_stars])
        
    # else:
    #     # Create csv file
    #     with open('data.txt', 'w') as csvfile:
    #         filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #         filewriter.writeheader(['Language', 'Stars'])
    #         filewriter.writerow([current_lang, total_stars])
        
    # # Append info into master_dict
    # # Labels: lang_name & sum_stars(for now)
    
    # # Create master list of data for graph
    # # master_list = []
    
    # # Create new dict to append to master_list
    # # temp_dict = {current_lang, total_stars}
    
    # # master_list.append(temp_dict)
    
    # # # Pass master_dict to index.html & d3 graph using flask
    # # ''' TODO '''
    
    
        
