from HDD import HDD
from OpticalDiscReader import OpticalDiscReader
from Powersupply import PowerSupply
from RAM import RAM
from Sensors import Sensors
from VideoCard import VideoCard


class Computer:
    def __init__(self):
        self.power_supply = PowerSupply()
        self.sensors = Sensors()
        self.video_card = VideoCard()
        self.ram = RAM()
        self.hdd = HDD()
        self.optical_disc_reader = OpticalDiscReader()

    def begin_work(self):
        print("Starting computer...")
        self.power_supply.apply_power()
        self.sensors.check_voltage()
        self.sensors.check_temperature("power supply")
        self.sensors.check_temperature("video card")
        self.power_supply.supply_power("video card")
        self.video_card.launch()
        self.video_card.check_connection()
        self.sensors.check_temperature("RAM")
        self.power_supply.supply_power("RAM")
        self.ram.launch_devices()
        self.ram.analyze_memory()
        self.video_card.display_data("RAM")
        self.power_supply.supply_power("disc reader")
        self.optical_disc_reader.startup()
        self.optical_disc_reader.check_disc_presence()
        self.video_card.display_data("disc reader")
        self.power_supply.supply_power("hard drive")
        self.hdd.launch()
        self.hdd.check_boot_sector()
        self.video_card.display_data("hard drive")
        self.sensors.check_all_systems_temperature()
        print("Computer successfully started.\n")

    def shut_down(self):
        print("Shutting down computer...")
        self.hdd.stop_device()
        self.ram.clear_memory()
        self.ram.analyze_memory()
        self.optical_disc_reader.return_to_original_position()
        self.power_supply.stop_power("video card")
        self.power_supply.stop_power("RAM")
        self.power_supply.stop_power("disc reader")
        self.power_supply.stop_power("hard drive")
        self.sensors.check_voltage()
        self.power_supply.shutdown()
        print("Computer successfully shut down.\n")