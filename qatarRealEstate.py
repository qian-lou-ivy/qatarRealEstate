#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Most updated Version

Created on Wed Jun  8 11:09:13 2022

@author: qianlou
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

# All the lists needed
ID = []
URL = []
Title_text = []
City = []
Location = []
Type = []
Furnished = []
Size_sqft = []
Size_sqm = []
Bedrooms = []
Bathrooms = []
Agent = []
Price = []
Photos = []

# there are 96 pages for now in the website

for page in range(96):
    
    # url will change in the for loop
    url = str('https://www.propertyfinder.qa/en/buy/properties-for-sale.html?page=' + str(page+1))
    
    # set up beautifulsoup
    property_page = requests.get(url)
    soup = BeautifulSoup(property_page.content,'html.parser')
    lists = soup.find_all('div', class_="card-list__item")
    
    for list in lists:
        Page_url = list.find('a', {"class":"card card--clickable"}).get("href")
        URL.append('https://www.propertyfinder.qa/' + Page_url)
        ID.append(re.findall(r'\d+','https://www.propertyfinder.qa/' + Page_url))
        title = list.find('h2', class_="card__title card__title-link").text.replace('\n', '')
        Title_text.append(title)
        full_location = list.find('span', class_="card__location-text").text.replace('\n', '')
        City.append(full_location.split(', ')[-1])
        Location.append(full_location.split(', ')[-2])
        price = list.find('span', class_="card__price-value").text.replace('\n', '')
        Price.append(price.replace(" ","")[0:-3])
        sqm = list.find('p', class_="card__property-amenity card__property-amenity--area").text.replace('\n','')
        Size_sqm.append(sqm[0:-4])
        typE = list.find('p', class_="card__property-amenity card__property-amenity--property-type").text.replace('\n','')
        Type.append(typE)
        Furnished.extend(" ")
        Bedrooms.extend(" ")
        Bathrooms.extend(" ")
        Agent.extend(" ")
        Photos.extend(" ")
        Size_sqft.extend(" ")
        
    if page == 1:
        break
        print("break")
    else:
        print("end")

        
        
real_dict = {'ID': ID, 'URL': URL, 'Title Text': Title_text, "City": City, "Location": Location,
        'Type': Type, 'Furnished': Furnished, 'Size (sq ft)': Size_sqft, 'Size (sqm)': Size_sqm,
        'Bedrooms': Bedrooms, 'Bathrooms': Bathrooms, 'Agent': Agent, 'Price': Price, 'Photos': Photos}

df = pd.DataFrame(real_dict)
df.to_csv('property_listings.csv')
        
        
        
        
        
        
        
        
        
        
        
        
        