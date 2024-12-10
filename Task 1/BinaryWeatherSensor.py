import random

# Existing System: Binary Weather Sensor
class BinaryWeatherSensor:
    def collect_data(self):
        # Simulating binary weather data as a byte string
        temp = random.randint(0, 50)  # Random temperature
        humidity = random.randint(0, 100)  # Random humidity
        return temp.to_bytes(2, 'big') + humidity.to_bytes(2, 'big')