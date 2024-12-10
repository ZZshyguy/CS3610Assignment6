class Sensors:
    def check_voltage(self):
        print("Sensors: Checking voltage.")

    def check_temperature(self, component):
        print(f"Sensors: Checking temperature in the {component}.")

    def check_all_systems_temperature(self):
        print("Sensors: Checking the temperature of all systems.")