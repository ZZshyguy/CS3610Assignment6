# Third-Party Library
class ThirdPartyForecastLibrary:
    def analyze_data(self, weather_data):
        print("Third-Party Forecast Library:")
        temperature = weather_data['temperature']
        humidity = weather_data['humidity']
        forecast = "Rainy" if humidity > 70 else "Sunny"
        print(f"Temperature: {temperature}°C, Humidity: {humidity}%, Forecast: {forecast}")