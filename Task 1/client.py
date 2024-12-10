from BinaryWeatherSensor import BinaryWeatherSensor
from WeatherDataAdapter import WeatherDataAdapter
from ThirdPartyForecastLibrary import ThirdPartyForecastLibrary
from WeatherApp import WeatherApp

sensor = BinaryWeatherSensor()
adapter = WeatherDataAdapter(sensor)
library = ThirdPartyForecastLibrary()
app = WeatherApp(adapter, library)

# Simulate displaying weather data and forecasting
app.display_data()