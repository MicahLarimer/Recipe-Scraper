import requests
from bs4 import BeautifulSoup
import json
import sqlite3

from insert_recipe import add_recipe  # type: ignore # Ensure correct import path

def scraper_recipe(url):
    #Send GET request to the website
    response = requests.get(url)
    
    #Check if the request was successful
    if response.status_code == 200:
        #Parse the HTML using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        #Extract the name of the recipe
        name = soup.find('h1', {'class': 'recipe-title'}).get_text(strip=True)
        
        #Extract ingredients(adapt based on website structure)
        ingredients = []
        ingredients_elements = soup.find_all('li', {'class': 'ingredient'})
        for ingredient in ingredients_elements:
            ingredients.append(ingredient.get_text(strip=True))  # Fix variable name
        ingredients_json = json.dumps(ingredients) #store as a JSON string
        
        #Extract instructions(again adapt based on website structure)
        instructions = []
        instruction_elements = soup.find_all('div', {'class': 'instruction'})
        for instruction in instruction_elements:
            instructions.append(instruction.get_text(strip=True))
            
        #Extract the cooking time
        cook_time = soup.find('span', {'class':'cook_time'}).get_text(strip=True)
        
        
        #Extract nutritional information
        nutrition = {}
        nutrition_elements = soup.find_all('span',{ 'class': 'nutrition-info'})
        for element in nutrition_elements:
            key = element.find('strong').get_text(strip=True)
            value = element.get_text(strip=True)
            nutrition[key] = value
        nutrition_json = json.dumps(nutrition)
        
        #Call add_recipe() function to insert data into the database
        add_recipe(name, ingredients_json, instructions, cook_time, nutrition_json)
        
    else:
        print(f"Failed to retrieve the webpage: {response.status_code}")
        
  # Correct function call
