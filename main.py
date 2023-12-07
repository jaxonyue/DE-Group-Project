from mylib.operations import (
    close_connection,
    read_wages_data_by_country,
    read_all_wages_data
)
from mylib.loadData import load

def main():
    # Load the dataset into the SQLite database
    load("dataset/Development of Average Annual Wages.csv")  # Import data from CSV

    # Print population data
    read_wages_data_by_country("France")

    read_all_wages_data()

    # Close the connection
    close_connection()
    return 1


if __name__ == "__main__":
    main()