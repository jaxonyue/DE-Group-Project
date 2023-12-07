from flask import Flask, jsonify, request, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/wages')
def get_wages():
    country = request.args.get('country')
    conn = sqlite3.connect('wages.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM wages WHERE Country=?', (country,))
    rows = cursor.fetchall()
    conn.close()
    # Assume that rows is a list of tuples with wage data
    data = {'years': ['2000', '2010', '2020', '2022'], 'wages': [row for row in rows]}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
