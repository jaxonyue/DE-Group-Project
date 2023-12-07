import csv
import sqlite3

# Extract, load, and merge the two wages datasets
def load(dataset_1, dataset_2):
    # Connect to SQLite database
    conn = sqlite3.connect('wages.db')
    cursor = conn.cursor()

    # Create a table named 'wages'
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS wages (
        Country TEXT PRIMARY KEY,
        Region TEXT,
        year_2000 DOUBLE,
        year_2010 DOUBLE,
        year_2020 DOUBLE,
        year_2022 DOUBLE
    )
    ''')

        # Load data from first CSV file
    with open(dataset_1, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            cursor.execute('''
            INSERT OR IGNORE INTO wages (Country, Region, year_2000, year_2010, year_2020) 
            VALUES (?, ?, ?, ?, ?)
            ''', (row["Country"], row["Region"], row["year_2000"], row["year_2010"], row["year_2020"]))

    # Load data from second CSV file, updating existing rows
    with open(dataset_2, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            cursor.execute('''
            UPDATE wages SET year_2022 = ? WHERE Country = ?
            ''', (row["year_2022"], row["Country"]))

    # Commit changes and close the SQLite connection
    conn.commit()
    conn.close()

