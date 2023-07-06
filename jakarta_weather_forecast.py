import requests
from datetime import datetime, timedelta

# OpenWeatherMap API key
api_key = "5da08e5ea7085a012c41d181ff31ad5e"

# URL to retrieve the weather forecast for Jakarta
url = f"http://api.openweathermap.org/data/2.5/forecast?q=Jakarta,id&units=metric&appid={api_key}"

# Send GET request to the API
response = requests.get(url)

# Check if the request is successful
if response.status_code == 200:
    # Retrieve weather data from the JSON response
    data = response.json()

    # Get the current date
    current_date = datetime.now().date()

    # Iterate over the next six days
    for day_offset in range(6):
        # Calculate the forecast date
        forecast_date = current_date + timedelta(days=day_offset)

        # Get the day from the forecast date
        day = forecast_date.strftime("%a")

        # Format the forecast date
        forecast_date_formatted = forecast_date.strftime("%d %b %Y")

        # Find the forecast data for the specific date
        forecast_data = [
            forecast for forecast in data["list"]
            if datetime.fromtimestamp(forecast["dt"]).date() == forecast_date
        ]

        # Calculate the average temperature for the specific date
        average_temperature = sum(
            forecast["main"]["temp"] for forecast in forecast_data
        ) / len(forecast_data)

        # Display the forecast day, date, and average temperature
        print(f"{day}, {forecast_date_formatted}: {average_temperature:.2f}°C")

else:
    print("Failed to retrieve weather data.")
