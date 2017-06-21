#!/usr/bin/env python3

import os
import re
from flask import Flask, jsonify, render_template, request, url_for
from flask_jsglue import JSGlue
import requests

# Create list of all languages used in Github to pass on to html page
'''TODO'''

# Get lang_name value from html buttons, ON CLICK
'''TODO'''
lang_name = request.form.get('lang_name')

# Make an api call and store the response
url = 'https://api.github.com/search/repositories?q=language:@lang_name&sort=stars'
r = requests.get(url)

if r.status_code != 200:
    raise RuntimeError("API Call status not OK")

# Store response in a variable 
response_dict = r.json()

# print("Total Repositories:", response_dict['total_count'])

# Explore info about repositories
# repo_dicts = response_dict['items']

# names, stars = [], []
# for repo_dict in repo_dicts:
#     names.append(repo_dict['name'])
#     stars.append(repo_dict['stargazers_count'])
    
# print("Repositories returned:", len(repo_dicts))

# print("\nSelected information about each repository:")
# for repo_dict in repo_dicts:
#     print("\nName:", repo_dict['name'])
#     print("Stars:", repo_dict['stargazers_count'])

# # Examine the first repository
# repo_dict = repo_dicts[0]
# print("\nKeys:", len(repo_dict))
# print("Repository Owner Name:", repo_dict['name'])
# print("Stargazer Count:", repo_dict['stargazers_count'])
# for key in sorted(repo_dict.keys()):
#     print(key)

languages = []

# Append info into master_dict
# Labels: lang_name & sum_stars & average_stars (for now)
''' TODO '''

# Pass master_dict to index.html & d3 graph using flask
''' TODO '''

if response_dict['incomplete_results'] != False:
    raise RuntimeError("'Incomplete Results' is True")
    
