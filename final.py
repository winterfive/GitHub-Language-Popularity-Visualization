#!/usr/bin/env python3

import requests
from flask import Flask, jsonify, render_template, request, url_for
from cs50 import SQL
from helpers import lookup

def main():
    
    """ This program creates a graph on which the user can plot the popularity (usage) 
        of specific programming languages on GitHub."""
    
    """ Create an empty graph on a webpage.
        The user can select buttons each labeled w/ a programming language, each a different color.
        First click will call an API request to GitHub and return w/ the # of time that language is selected.
        language data will be stored in a row in a SQLite table.
        The graph will be updated via a query to the table.
        Second click will delete that languages row from the table and update the graph accordingly """
    
    lang = "python"
    
    # make API call and store response
    url = "https://api.github.com/search/repositories?q=language:{0}".format(lang)
    r = requests.get(url)
    print("Status code:", r.status_code)
    
    # store API response in a var
    response_dict = r.json()
    
    # process results
    print(response_dict.keys())
    print("Total repositories:", response_dict['total_count'])
    
    # Explore info about repositories
    repo_dicts = response_dict['items']
    print("Repositories returned:", len(repo_dicts))
    
    # Examine the first repo returned
    repo_dict = repo_dicts[0]
    print("\nKeys:", len(repo_dict))
    for key in sorted(repo_dict.keys()):
        print(key)

if __name__ == "__main__":
    main()
