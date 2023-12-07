from flask import Flask, jsonify, request, render_template
from mylib.operations import read_wages_data_by_country, read_all_wages_data
from mylib.loadData import load

app = Flask(__name__)

load(
    dataset_1="dataset/Development of Average Annual Wages_1.csv",
    dataset_2="dataset/Development of Average Annual Wages_2.csv",
)


@app.route("/")
def index():
    all_data = read_all_wages_data()
    countries = [data[0] for data in all_data]
    countries.sort()
    return render_template("index.html", countries=countries)


@app.route("/api/wages")
def get_wages():
    country = request.args.get("country")
    # Use the imported function to get the wage data for the country
    data = read_wages_data_by_country(country)
    # Transform data into the expected format
    if data:
        # Assuming the data is a tuple in the form (id, country, year_2000, year_2010, year_2020, year_2022)
        formatted_data = {
            "years": ["2000", "2010", "2020", "2022"],
            "wages": data[2:],  # This slices the tuple to only include wage data
        }
        return jsonify(formatted_data)
    else:
        return jsonify({"error": "Data not found for the selected country"}), 404


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=7000)
