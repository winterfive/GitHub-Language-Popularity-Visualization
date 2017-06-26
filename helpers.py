#!/usr/bin/python

from flask import render_template
import requests

def lookup(n):
    """Run API call for language selected"""

    # query GitHub for info
    # Make an api call and store the response
    url = 'https://api.github.com/search/repos?q=language:{}&sort=stars'.format(n)
    r = requests.get(url)
    r.json()
    
    # ensure r exists
    try:
        keys = r.keys()
    except:
        return None
        
    # check r
    if r.status_code != 200:
        raise RuntimeError('API Call status not OK')
        return None
    
    if r['incomplete_results'] != False:
        raise RuntimeError("'Incomplete Results' is True")
        return None
        
    # Create stars sum variable
    total_stars = 0
        
    # Create and store total # of stars in variable, total_stars
    items = r['items']
    for item in items:
        total_stars += int(items['stargazers_count'])
        
    # return total # of stars
    return total_stars
    
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
