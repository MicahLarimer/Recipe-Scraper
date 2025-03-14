import sqlite3

conn = sqlite3.connect('recipes.db')

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS recipes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    ingredients TEXT,
    instructions TEXT,
    cook_time INTEGER,
    nutrition TEXT
)""")

conn.commit()
conn.close()