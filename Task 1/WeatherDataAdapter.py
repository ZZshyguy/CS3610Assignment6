from BinaryWeatherSensor import BinaryWeatherSensor

# Adapter: Translates Binary Data to XML
class WeatherDataAdapter:
    def __init__(self, sensor: BinaryWeatherSensor):
        self.sensor = sensor

    def get_weather_data(self):
        binary_data = self.sensor.collect_data() #collect binary data from the sensor
        temperature = int.from_bytes(binary_data[:2], 'big') #convert format
        humidity = int.from_bytes(binary_data[2:], 'big') #convert format
        return {"temperature": temperature, "humidity": humidity}