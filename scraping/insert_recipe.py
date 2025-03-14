import sqlite3

# Function to add a recipe to the database
def add_recipe(name, ingredients, instructions, cook_time, nutrition):
    # Connect to the database
    conn = sqlite3.connect('recipes.db')
    cursor = conn.cursor()

    # SQL Insert statement
    sql = "INSERT INTO recipes (name, ingredients, instructions, cook_time, nutrition) VALUES (?, ?, ?, ?, ?)"
    data = (name, ingredients, instructions, cook_time, nutrition)

    # Execute the SQL statement with the data
    cursor.execute(sql, data)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
