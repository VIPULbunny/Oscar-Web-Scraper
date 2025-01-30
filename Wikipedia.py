''' 
Repository: Oscar-Web-Scraper
File: oscar_scraper.py
Description: This script scrapes the Wikipedia page listing Academy Award-winning films and extracts details such as the film name, year of award, number of awards won, and nominations received.
'''

# Importing necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from bs4 import BeautifulSoup
import requests
import re

# Wikipedia URL containing Oscar-winning films
url = "https://en.wikipedia.org/wiki/List_of_Academy_Award%E2%80%93winning_films"
req = requests.get(url)

# Parsing the webpage content using BeautifulSoup
soup = BeautifulSoup(req.content, 'html.parser')

# Lists to store extracted data
Film = []        # Stores film names
Year = []        # Stores award-winning years
Award = []       # Stores the number of awards won
Nomination = []  # Stores the number of nominations received
count = 0        # Counter to track column position in the table

# Extracting table data
for i in soup.find_all('td'):
    i = re.sub('^<td>.*">|<td>|</td>|<.*>|\n', "", str(i))  # Cleaning HTML tags
    
    if count == 0:
        Film.append(i)
        count += 1
    elif count == 1:
        Year.append(i)
        count += 1
    elif count == 2:
        Award.append(i)
        count += 1
    else:
        Nomination.append(i)
        count = 0  # Reset counter after collecting all four columns

# Creating a DataFrame from extracted data
# Limiting data to first 1373 entries to avoid potential inconsistencies
oscar_data = {"Film": Film[:1373], "Year": Year[:1373], "Award": Award[:1373], "Nomination": Nomination[:1373]}
oscar_df = pd.DataFrame(oscar_data, columns=['Film', 'Year', 'Award', 'Nomination'])

# Display the last 10 entries of the scraped data
print(oscar_df)