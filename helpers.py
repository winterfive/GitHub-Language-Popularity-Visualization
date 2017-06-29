#!/usr/bin/python

from flask import render_template
import requests
import csv
import os.path
import pathlib

def lookup(n):
    """Run API call for language selected"""
    
    # query GitHub for info
    # Make an api call and store the response
    url = 'https://api.github.com/search/repositories?q=language:{}&sort=stars'.format(n)
    r = requests.get(url)
    
    # check r
    if r.status_code != 200:
        raise RuntimeError('API Call status not OK')
        return 3
        
    r = r.json()
    
    # ensure r exists
    try:
        keys = r.keys()
    except:
        return 2
        
    if r['incomplete_results'] != False:
        raise RuntimeError("'Incomplete Results' is True")
        return 4
        
    # Create stars sum variable
    total_stars = 0
    
    # Create and store total # of stars in variable, total_stars
    repo_dicts = r['items']
    for repo_dict in repo_dicts:
        total_stars += int(repo_dict['stargazers_count'])
        
    # get average stars per repository
    total_stars = round(total_stars / 30)
        
    # write data to csv file
    ofile = open('data.csv', "a")
    writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    
    # write specific info into csv
    writer.writerow([n , total_stars])
     
    # ifile.close()
    ofile.close()
        
    # return total # of stars
    # return total_stars
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
    """Erases all data from csv file"""
    f = open("data.csv", "w")
    f.truncate()
    f.close()
