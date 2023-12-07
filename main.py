from mylib.operations import (
    read_wages_data_by_country,
    read_all_wages_data
)
from mylib.loadData import load
import sqlite3


def main():
    # Load the dataset into the SQLite database
    load()  # Import data from CSVs

    # Print population data
    #print(read_wages_data_by_country("France"))

    print(read_all_wages_data())

    # Close the connection
    return 1

def get_wages():
    conn = sqlite3.connect('wages.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM wages WHERE Country=?', ('Canada',))
    rows = cursor.fetchall()
    conn.close()
    # Assume that rows is a list of tuples with wage data
    data = {'years': ['2000', '2010', '2020', '2022'], 'wages': [row for row in rows]}
    print(data)

if __name__ == "__main__":
    main()
