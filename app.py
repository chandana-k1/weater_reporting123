
from flask import Flask, jsonify, request
import csv

app = Flask(__name__)

# Load the data from the CSV file
data = []
with open('weather_data.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

# API endpoint to get weather details by date
@app.route('/weather/date/<date>', methods=['GET'])
def get_weather_by_date(date):
    result = [entry for entry in data if entry['Date'] == date]
    return jsonify(result)

# API endpoint to get weather details by month
@app.route('/weather/month/<year>/<month>', methods=['GET'])
def get_weather_by_month(year, month):
    result = [entry for entry in data if entry['Date'].startswith(f"{year}-{month:02d}")]
    return jsonify(result)

# API endpoint to get temperature statistics by year
@app.route('/weather/stats/<year>', methods=['GET'])
def get_temperature_stats(year):
    year_data = [entry for entry in data if entry['Date'].startswith(f"{year}")]
    temperatures = [float(entry['Temperature']) for entry in year_data]
    if temperatures:
        high = max(temperatures)
        median = sorted(temperatures)[len(temperatures) // 2]
        low = min(temperatures)
        return jsonify({'high': high, 'median': median, 'low': low})
    else:
        return jsonify({'error': 'No data found for the given year'})

if __name__ == '__main__':
    app.run(debug=True)
