#!/usr/bin/python

from flask import render_template
from cs50 import SQL
import requests
import csv
# import os.path
# import pathlib

# create variable for sqlite table connection
db = SQL("sqlite:///data.db")

def lookup(n):
    """Run API call for language selected"""
    
    # query GitHub for info
    # Make an api call and store the response
    url = "https://api.github.com/search/repositories?q=language:{}&sort=stars".format(n)
    r = requests.get(url)
    
    # check r
    if r.status_code != 200:
        raise RuntimeError("API Call status not OK")
        return 3
        
    r = r.json()
    
    # ensure r exists
    try:
        keys = r.keys()
    except:
        return 2
        
    if r["incomplete_results"] != False:
        raise RuntimeError("Incomplete Results is True")
        return 4
        
    # Create stars sum variable
    total_stars = 0
    
    # Create and store total # of stars in variable, total_stars
    repo_dicts = r["items"]
    for repo_dict in repo_dicts:
        total_stars += int(repo_dict["stargazers_count"])
        
    # get average stars per repository
    total_stars = round(total_stars / 30)
    
    # if n is cpp, change to c++
    if n == "cpp":
        n = "c++"
    
    # check if table exists already, if not, create
    db.execute("CREATE TABLE IF NOT EXISTS githubData (langName CHAR(20) UNIQUE, stars INTEGER)")
    
    # place new data in sqlite table
    db.execute("INSERT OR REPLACE INTO githubData (langName, stars) VALUES(:langName, :stars)",\
        langName = n,\
        stars = total_stars)
    
    # fill json cs via sqlite table
    items = db.execute("SELECT * FROM githubData")
    
    '''yes, I know data.csv doesn't belong in static but I cannot make
    changes to the web container so I have to do it this way for this assignment'''
    with open("static/data.csv", "wt", newline="") as f:
        writer = csv.DictWriter(f, ["langName", "stars"])
        writer.writeheader()
        for item in items:
            writer.writerow(item)
    
    return
    
def nope(top="", bottom=""):
    """Renders message as an error tracker."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
            ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("nope.html", top=escape(top), bottom=escape(bottom))
    
def erase_csv():
    """Erases all data from sqlite table"""
    """Deletes csv file"""
    
    # delete rows from table
    db.execute("DELETE FROM githubData")
    
    # delete data from csv file
    f = open("static/data.csv", "r+")
    f.truncate()
    f.close()
    
    
