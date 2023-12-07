from flask import Flask, jsonify, request, render_template
from mylib.operations import read_wages_data_by_country

app = Flask(__name__)

@app.route('/')
def index():
    countries = ["Iceland", "Luxembourg", "United States", "Switzerland", "Belgium", 
    "Denmark", "Austria", "Netherlands", "Australia", "Canada", "Germany", 
    "United Kingdom", "Norway", "France", "Ireland", "Finland", "New Zealand", 
    "Sweden", "South Korea", "Slovenia", "Italy", "Israel", "Lithuania", 
    "Spain", "Japan", "Poland", "Estonia", "Latvia", "Czech Republic", 
    "Chile", "Costa Rica", "Portugal", "Hungary", "Slovakia", "Greece", "Mexico"]
    return render_template('index.html', countries=countries)

@app.route('/api/wages')
def get_wages():
    country = request.args.get('country')
    # Use the imported function to get the wage data for the country
    data = read_wages_data_by_country(country)
    # Transform data into the expected format
    if data:
        # Assuming the data is a tuple in the form (id, country, year_2000, year_2010, year_2020, year_2022)
        formatted_data = {
            'years': ['2000', '2010', '2020', '2022'],
            'wages': data[1:]  # This slices the tuple to only include wage data
        }
        return jsonify(formatted_data)
    else:
        return jsonify({'error': 'Data not found for the selected country'}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=7000)
