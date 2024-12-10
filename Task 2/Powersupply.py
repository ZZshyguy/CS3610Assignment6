class PowerSupply:
    def apply_power(self):
        print("Power supply: Applying power.")

    def supply_power(self, component):
        print(f"Power supply: Supplying power to the {component}.")

    def stop_power(self, component):
        print(f"Power supply: Stopping power to the {component}.")

    def shutdown(self):
        print("Power supply: Shutdown.")