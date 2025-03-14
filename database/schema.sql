import sqlite3

CREATE TABLE [IF NOT EXISTS] recipes (
    INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NO NULL,
    ingredients TEXT,
    instructions,
    cook_time INTEGER,
    nutrition TEXT
);