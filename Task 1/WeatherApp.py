from WeatherDataAdapter import WeatherDataAdapter
from ThirdPartyForecastLibrary import ThirdPartyForecastLibrary

# Weather App: Displays Data
class WeatherApp:
    def __init__(self, adapter: WeatherDataAdapter, library: ThirdPartyForecastLibrary):
        self.adapter = adapter
        self.library = library

    def display_data(self):
        # Fetch and convert data using the adapter
        weather_data = self.adapter.get_weather_data()
        print("Weather App:")
        print(f"Temperature: {weather_data['temperature']}°C")
        print(f"Humidity: {weather_data['humidity']}%")
        # Use the third-party library to analyze and display a forecast
        self.library.analyze_data(weather_data)