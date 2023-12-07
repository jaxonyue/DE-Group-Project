import sqlite3

# Establish a connection
conn = sqlite3.connect('wages.db')
cursor = conn.cursor()

# READ: Get all data
def read_all_wages_data():
    cursor.execute("SELECT * FROM wages")
    return cursor.fetchall()

def read_wages_data_by_country(country):
    # Create a new connection for each call to this function
    conn = sqlite3.connect('wages.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM wages WHERE country=?", (country,))
    data = cursor.fetchone()
    conn.close()  # Close the connection after the operation is done
    return data

# Close the connection (Make sure to call this when done with database operations)
def close_connection():
    conn.close()
