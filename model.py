from enum import Enum

class Vehicle:
    # TODO Vehicle implementation
    def __init__(self, vehicle_id, manufacturer, model, horse_power, mileage, color, price, production_year, fuel_type, transmission):
        self.__vehicle_id = vehicle_id
        self.__manufacturer = manufacturer
        self.__model = model
        self.__horse_power = horse_power
        self.__mileage = mileage
        self.__price = price
        self.__production_year = production_year
        self.__transmission = transmission
        self.__color = color
        self.__fuel_type = fuel_type
    
	# TODO add attributes and Getters / Setters
    
    # Vehicle Id Get & Set
    def get_vehicle_id(self):
        return self.__vehicle_id
    def set_vehicle_id(self, vehicle_id):
        self.__vehicle_id = vehicle_id

    # Manufacturer Get & Set
    def get_manufacturer(self):
        return self.__manufacturer
    def set_manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer
    
    # Model Get & Set
    def get_model(self):
        return self.__model
    def set_model(self, model):
        self.__model = model

    # Horse Power Get & Set
    def get_horse_power(self):
        return self.__horse_power
    def set_model(self, horse_power):
        self.__horse_power = horse_power

    # Mileage Get & Set
    def get_mileage(self):
        return self.__mileage
    def set_model(self, mileage):
        self.__mileage = mileage
    
    # Color Year Get & Set
    def get_color(self):
        return self.__color
    def set_color(self, color):
        self.__color = color

    # Price Get & Set
    def get_price(self):
        return self.__price
    def set_price(self, price):
        self.__price = price

    # Production Year Get & Set
    def get_production_year(self):
        return self.__production_year
    def set_production_year(self, production_year):
        self.__production_year = production_year

    # Fuel Type Year Get & Set
    def get_fuel_type(self):
        return self.__fuel_type
    def set_fuel_type(self, fuel_type):
        self.__fuel_type = fuel_type

    # Transmission Year Get & Set
    def get_transmission_type(self):
        return self.__transmission
    def set_transmission_type(self, transmission):
        self.__transmission = transmission

class Color(Enum):
    # TODO define color enumeraition literals 
    BLACK = 1
    GREY = 2
    WHITE = 3
    BLUE = 4
    RED = 5
    BROWN = 6
    YELLOW = 7

class FuelType(Enum):
    GASOLINE = 1
    DIESEL_FUEL = 2

class Manufacturer(Enum):
    # TODO define manufacturer enumeraition literals
    AUDI = 1
    BMW = 2
    VW = 3
    HONDA = 4
    SKODA = 5

class Transmission(Enum):
    # TODO define transmission enumeraition literals 
    AUTOMATIC = 1
    MANUAL = 2