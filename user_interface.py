from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp 
from kivy.core.window import Window
from kivy.lang import Builder

from controller import VehicleFileManager, VehicleTransformer
from model import Vehicle

from functools import partial

class VehicleShop(MDApp):
    file_path = "vehicle-list.csv"
    table = VehicleTransformer()

    __selected_row = []
    selected_row = []
    def build(self):
        Window.size = (900, 700)

        self.screen = Builder.load_file("user_interface_gui.kv")

        first_box_layout = self.screen.ids.first_box_layout
        second_box_layout = self.screen.ids.second_box_layout

        row_data = self.update_table_data()

        self.vehicle_table = MDDataTable(
            pos_hint = {'center_x': 0.5, 'center_y': 0.5},
            size_hint = (1, 1),
            check = False,
            rows_num = len(row_data) if row_data else 0,
            column_data = [
                ("ID", dp(25)),
                ("Manufacturer", dp(30)),
                ("Model", dp(25)),
                ("Horse Power", dp(25)),
                ("Mileage", dp(25)),
                ("Color", dp(25)),
                ("Price", dp(25)),
                ("Production Year", dp(25)),
                ("Fuel Type", dp(25)),
                ("Trasmission", dp(30))
            ],
            row_data = row_data
        )
        first_box_layout.add_widget(self.vehicle_table)
        self.vehicle_table.bind(on_row_press=self.on_row_press)


        self.order_table = MDDataTable(
            pos_hint = {'center_x': 0.5, 'center_y': 0.5},
            size_hint = (1, 1),
            rows_num = len(row_data),
            check = False,
            column_data = [
                ("ID", dp(25)),
                ("Manufacturer", dp(30)),
                ("Model", dp(25)),
                ("Horse Power", dp(25)),
                ("Mileage", dp(25)),
                ("Color", dp(25)),
                ("Price", dp(25)),
                ("Production Year", dp(25)),
                ("Fuel Type", dp(25)),
                ("Trasmission", dp(30))
            ],
            row_data = []
        )
        second_box_layout.add_widget(self.order_table)
   
        return self.screen




    def on_row_press(self, instance_table, instance_row):
        row_num = int(instance_row.index/len(instance_table.column_data))
        selected_row = instance_table.row_data[row_num]

        if selected_row not in self.__selected_row:
            self.__selected_row.append(instance_table.row_data[row_num])
        else:
            return

    def add_order(self):

        if len(self.__selected_row) == 0:
            return 

        for row in self.__selected_row:
            self.order_table.row_data.append(row)
            if row in self.vehicle_table.row_data:
                self.vehicle_table.row_data.remove(row)

        self.order_table.update_row_data
        self.vehicle_table.update_row_data


        self.__selected_row.clear()

    def update_table_data(self):
        list_importer = VehicleFileManager(self.file_path)
        list = list_importer.import_vehicles_from_file(self.file_path)
        table_data = self.table.transform_data_as_string_array_to_vehicle_objects(list)
        
        row_data = []

        if not table_data:
            return []
        else:
            for rows in table_data:
                if isinstance (rows, Vehicle):
                    row_data.append((rows.get_vehicle_id(), rows.get_manufacturer(), rows.get_model(), rows.get_horse_power(), rows.get_mileage(), rows.get_color(), rows.get_price(), rows.get_production_year(), rows.get_fuel_type(), rows.get_transmission_type()))

            return row_data



    def calculate_amount(self):
        if not self.order_table.row_data:
            return
        else:

            invoice_label = self.screen.ids.invoice
            invoice_text = ""
            total_price = 0
            if self.order_table.row_data:
                for row in self.order_table.row_data:
                    name = row[2]
                    price = row[6]
                    total_price += price
                    invoice_text += f"    {name}            {price}     \n"
            text = (
                f"                     Vehicle Shop                      \n"
                f"-------------------------------------------------------\n"
                f"       Name                |                Price      \n"
                f"-------------------------------------------------------\n"
                f"{invoice_text}"
                f"-------------------------------------------------------\n"
                f"      Total                |        {total_price}        "
            )
            invoice_label.text = text


            list_importer = VehicleFileManager(self.file_path)
            
            stringify_list = self.table.transform_data_as_string_array_to_vehicle_objects(self.vehicle_table.row_data)
            list_importer.rewrite_file(stringify_list)

            self.order_table.row_data = []
            self.vehicle_table.row_data = self.update_table_data()


    def app_refresh(self):
        self.order_table.row_data = []
        self.vehicle_table.row_data = []

        self.__selected_row = []
        self.vehicle_table.row_data = self.update_table_data()

VehicleShop().run()
