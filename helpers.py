#!/usr/bin/python

import csv
import urllib.request
from flask import render_template

# from flask import redirect, render_template, request, session, url_for
# from functools import wraps

def lookup(n):
    """Run API call for language selected"""

    # query GitHub for info
    # Make an api call and store the response
    try:
        url = "https://api.github.com/search/repositories?q=language:{}&sort=stars".format(n)
        webpage = urllib.request.urlopen(url)
        datareader = csv.reader(webpage.read().decode("utf-8").splitlines())
        r = next(datareader)
    except:
        return None
        
    # ensure file exists
    try:
        keys = r.keys()
    except:
        return None
        
    # check response
    if r.status_code != 200:
        raise RuntimeError("API Call status not OK")
        return None
    
    if r['incomplete_results'] != False:
        raise RuntimeError("'Incomplete Results' is True")
        
    # Create stars sum variable
    total_stars = 0
        
    # Create and store total # of stars in variable, total_stars
    items = r['items']
    for item in items:
        total_stars += int(items['stargazers_count'])
        
    # return total # of stars
    return total_stars
    
def apology(top="", bottom=""):
    """Renders message as an apology to user."""
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
