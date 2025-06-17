# Weather Data Processing and API
This project processes a dummy weather dataset for Delhi spanning 20 years, stores it efficiently, and provides an API to retrieve weather details by date or month, and temperature statistics by year.
## How to Run
1. Install the required packages: `pip install flask`
2. Run the Flask app: `python app.py`
3. Use the following API endpoints:
   - `/weather/date/<date>`: Get weather details by date
   - `/weather/month/<year>/<month>`: Get weather details by month
   - `/weather/stats/<year>`: Get temperature statistics by year
