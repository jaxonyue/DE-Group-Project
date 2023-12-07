import sqlite3

# CREATE: Insert a new country's data
def create_wages_data(country, year_2000, year_2010, year_2020, year_2022):
    conn = sqlite3.connect('wages.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO wages (country, year_2000, year_2010, year_2020, year_2022) VALUES (?, ?, ?, ?, ?)', 
                   (country, year_2000, year_2010, year_2020, year_2022))
    conn.commit()
    cursor.close()
    data = [country, year_2000, year_2010, year_2020, year_2022]
    print("Wages data created: " + ', '.join(map(str, data)))

# READ: Get all data
def read_all_wages_data():
    conn = sqlite3.connect('wages.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM wages")
    data = cursor.fetchall()
    cursor.close()
    return data

def read_wages_data_by_country(country):
    # Create a new connection for each call to this function
    conn = sqlite3.connect('wages.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM wages WHERE country=?", (country,))
    data = cursor.fetchone()
    conn.close()  # Close the connection after the operation is done
    return data

# UPDATE: Update data based on the country
def update_wages_data(country, year_2000, year_2010, year_2020, year_2022):
    conn = sqlite3.connect('wages.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE wages SET year_2000=?, year_2010=?, year_2020=?, year_2022=? WHERE country=?", 
                   (country, year_2000, year_2010, year_2020, year_2022))
    conn.commit()
    conn.close()
    data = [country, year_2000, year_2010, year_2020, year_2022]
    print("Wages data for " + country + " successfully updated to: " + ', '.join(map(str, data)))

# DELETE: Delete data by country
def delete_wages_data(country):
    conn = sqlite3.connect('wages.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM wages WHERE country=?", (country,))
    conn.commit()
    conn.close()
    print("Wages data for " + country + " deleted")
