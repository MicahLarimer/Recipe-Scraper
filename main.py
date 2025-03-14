from scraper import scrape_recipe  # Import the scraper function

def main():
    url = input("Enter the recipe URL: ")  # Ask user for the recipe URL
    recipe = scrape_recipe(url)  # Call the scraper function

    if recipe:
        print("\n📌 Recipe Extracted:\n")
        print("Title:", recipe.get("title", "N/A"))
        print("\nIngredients:")
        for ingredient in recipe.get("ingredients", []):
            print("-", ingredient)
        
        print("\nInstructions:")
        print(recipe.get("instructions", "N/A"))
    else:
        print("❌ Failed to extract recipe. Please check the URL.")

if __name__ == "__main__":
    main()
