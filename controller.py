# prepared import of enumerations
from model import Color, FuelType, Manufacturer, Transmission, Vehicle
# prepared csv module import
import csv
from typing import List

class VehicleFileManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def import_vehicles_from_file(self, file_path):
        # TODO read vehicle-list.csv and transform to String array
        vehicles = []
        
        with open(file_path, mode="r") as vehicle_file:
            csv_reader = csv.reader(vehicle_file)
            for row in csv_reader:
                vehicles.append(row)

        return vehicles
    

    def rewrite_file(self, vehicle_list):
        # TODO write back into vehicle-list.csv and transform to String array
	    # TODO call method prepare_the_vehicle_for_rewriting(String, Vehicle)
        print(vehicle_list)
        with open(self.file_path, mode="w", newline="") as vehicle_file:
            csv_writer = csv.writer(vehicle_file)
            for vehicle in vehicle_list: 
                if isinstance(vehicle, Vehicle):
                    vehicle_string = self.prepare_the_vehicle_for_rewriting(vehicle.get_vehicle_id(), vehicle)
                    csv_writer.writerow(vehicle_string)
        
    def prepare_the_vehicle_for_rewriting(self, vehicle_id, vehicle):
        #  TODO add vehicle attribute information to vehicle_string_for_rewrite
		# Hint: vehicle_string_for_rewrite.join(String)
        vehicle_string_for_rewrite = [
            vehicle_id, vehicle.get_manufacturer(), vehicle.get_model(), vehicle.get_horse_power(), vehicle.get_mileage(), vehicle.get_color(), vehicle.get_price(), vehicle.get_production_year(), vehicle.get_fuel_type(),vehicle.get_transmission_type()
        ]
        return vehicle_string_for_rewrite
    
class VehicleShopPrinter:
    
    def print_available_vehicles(self, vehicle_list):
        # TODO Implement print available vehicles
        if vehicle_list is None:
            print("No vehicles is available")
        else: 
            print("\nAvailable Vehicles: \n")
            for vehicle in vehicle_list:
                if isinstance(vehicle, Vehicle):
                    print(
                        f"----------------------------------------------------------------------------------------------\n"
                        f"{int(vehicle.get_vehicle_id()):<5}|"
                        f"{vehicle.get_manufacturer():<10}|"
                        f"{str(vehicle.get_model()):<10}|"
                        f"{int(vehicle.get_horse_power()):<5}|"
                        f"{int(vehicle.get_mileage()):<8}|"
                        f"{vehicle.get_color():<10}|"
                        f"{float(vehicle.get_price()):<8}|"
                        f"{int(vehicle.get_production_year()):<5}|"
                        f"{str(vehicle.get_fuel_type()):<12}|"
                        f"{vehicle.get_transmission_type():<10}"
                        f"\n----------------------------------------------------------------------------------------------"
                    )
       
    def print_vehicle_id_to_sell_message(self):
        print("\n\n Please enter the number (ID) of the vehicle you want to sell: ")

class VehicleShopProcessor:

    # responsible to sell a specified vehicle by id

    def sell_vehicle(self, vehicle_list, selected_vehicle_id):
    # TODO selling a vehicle means to remove it from the available vehicle list
        for index, vehicle in enumerate(vehicle_list):
            if isinstance(vehicle, Vehicle):
                if vehicle.get_vehicle_id() == selected_vehicle_id:
                    print("\nVehicle with ID", vehicle.get_vehicle_id(), "was sold.")
                    vehicle_list.pop(index)
                    break
        print("The entered Id doesnt match any of the cars Id.")
            

class VehicleTransformer:

    # transforms a data array into a {@link Vehicle} list 
	# @param vehicle data array
	# @return list of {@link Vehicle} objects

    def transform_data_as_string_array_to_vehicle_objects(self, vehicles_as_string_array: List[str]) -> List[Vehicle]:
        # TODO take data from String list and transform to list of vehicle objects
        # TODO call method transformToVehicleObject
        # Hint: use for loop

        vehicle_objects = []
        for vehicle_string in vehicles_as_string_array:
            vehicle_object = self.transform_to_vehicle_object(vehicle_string)
            vehicle_objects.append(vehicle_object)

        return vehicle_objects

    # transforms a vehicle data record as String into a {@link Vehicle} object
	# @param vehicle data record as String 
	# @return {@link Vehicle} object 
    
    def transform_to_vehicle_object(self, vehicle_as_string_array: str) -> Vehicle: 
        # TODO transform the vehicle as string into a vehicle object

        vehicle_id = int(vehicle_as_string_array[0])
        manufacturer = self.get_manufacturer_from_string(vehicle_as_string_array[1])
        model = str(vehicle_as_string_array[2])
        horse_power = int(vehicle_as_string_array[3])
        mileage = int(vehicle_as_string_array[4])
        color = self.get_car_color_from_string(vehicle_as_string_array[5])
        price = int(vehicle_as_string_array[6])
        production_year = int(vehicle_as_string_array[7]) 
        fuel_type = self.get_fuel_type_from_string(vehicle_as_string_array[8])
        transmission = self.get_transmission_from_string(vehicle_as_string_array[9])

    
        vehicle = Vehicle(vehicle_id, manufacturer, model, horse_power, mileage, color, price, production_year, fuel_type, transmission)
        return vehicle
    
    # Converts a string representation of a Manufacturer to its corresponding Manufacturer enumeration value
    def get_manufacturer_from_string(self, manufacturer_as_string):
        for manufacturer in Manufacturer:
            if manufacturer.name == manufacturer_as_string:
                return manufacturer_as_string
            
        raise ValueError("Manufacturer not supported: " + manufacturer_as_string)

    # Converts a string representation of a color to its corresponding ColorType enumeration value
    def get_car_color_from_string(self, color_as_string): 
        for color in Color:
            if color.name == color_as_string:
                return color_as_string
            
        raise ValueError("Color is not supported: " + color_as_string)

    # Converts a string representation of a fuel type to its corresponding FuelType enumeration value
    def get_fuel_type_from_string(self, fuel_type_as_string):
        for fuel_type in FuelType:
            if fuel_type.name == fuel_type_as_string:
                return fuel_type_as_string
            
        raise ValueError("Fuel Type is not supported: " + fuel_type_as_string)
    
    # Converts a string representation of a transmission to its corresponding Transmission enumeration value
    def get_transmission_from_string(self, transmission_as_string):
        for transmission in Transmission:
            if transmission.name == transmission_as_string:
                return transmission_as_string
            
        raise ValueError("Transmission is not supported: " + transmission_as_string)