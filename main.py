# # Blood Donation System
#
# import json
#
#
# def load_data():
#
#     try:
#         with open('New_Donor_Data.json', 'r') as file:
#             return json.load(file)
#     except FileNotFoundError:
#         return []
#
#
# def save_data_helper(donorData):
#
#     with open('New_Donor_Data.json', 'w') as file:
#         json.dump(donorData, file)
#
#
# def is_valid_id(ID):
#
#     if len(str(ID)) != 4:
#         print("*" * 22)
#         print("Invalid ID: ID must be 4 digits long.")
#         print("*" * 22)
#         return exit()
#
#
# def is_digit(*args):
#
#     arg = ''.join(str(arg) for arg in args)
#     if arg.isdigit():
#         print("*" * 22)
#         print("Invalid Index")
#         print("*" * 22)
#         return exit()
#
#
# def is_duplicate(donorData, ID):
#
#     for data in donorData:
#         if data['id'] == ID:
#             print("*" * 22)
#             print("Please enter the different ID.")
#             print("*" * 22)
#             return exit()
#
#
# def add_donor(donorData):
#
#     ID = int(input("Enter 4 digits ID: "))
#     is_valid_id(ID)
#     is_duplicate(donorData, ID)
#
#     name = input("Enter Name: ")
#     is_digit(name)
#
#     age = int(input("Enter Age: "))
#     cellNo = int(input("Enter CellNo: "))
#     city = input("Enter City: ")
#     is_digit(city)
#
#     bloodGroup = input("Enter BloodGroup: ")
#     is_digit(bloodGroup)
#
#     print("*" * 22)
#     print(f"Donor data has been inserted successfully.")
#     print("*" * 22)
#     print("\n")
#
#     donorData.append({'id': ID, 'name': name, 'age': age, 'cellNo': cellNo, 'city': city, 'bloodGroup': bloodGroup})
#     save_data_helper(donorData)
#
#
# def search_donor(donorData):
#
#     ID = int(input("Enter Donor ID: "))
#     is_valid_id(ID)
#
#     for data in donorData:
#         if data['id'] == ID:
#             print(f"Name: {data['name']}")
#             print(f"Age: {data['age']}")
#             print(f"CellNo: 0{data['cellNo']}")
#             print(f"City: {data['city']}")
#             print(f"BloodGroup: {data['bloodGroup']}")
#             return []
#     print("ID not found.")
#     return exit()
#
#
# def update_donor(donorData):
#
#     ID = int(input("Enter Donor ID: "))
#     is_valid_id(ID)
#
#     for data in donorData:
#         if data['id'] == ID:
#             ID = int(input("Enter new 4 digits ID: "))
#             is_valid_id(ID)
#
#             name = input("Enter Name: ")
#             is_digit(name)
#
#             age = int(input("Enter Age: "))
#             cellNo = int(input("Enter CellNo: "))
#             city = input("Enter City: ")
#             is_digit(city)
#
#             bloodGroup = input("Enter BloodGroup: ")
#             is_digit(bloodGroup)
#
#             print("*" * 22)
#             print(f"Donor with ID {ID} has been updated successfully.")
#             print("*" * 22)
#             print("\n")
#
#             data.update({'id': ID, 'name': name, 'age': age, 'cellNo': cellNo, 'city': city, 'bloodGroup': bloodGroup})
#             save_data_helper(donorData)
#
#
# def delete_donor(donorData):
#
#     ID = int(input("Enter Donor ID: "))
#     is_valid_id(ID)
#
#     donorFound = False
#
#     for data in donorData:
#         if data['id'] == ID:
#             donorData.remove(data)
#             donorFound = True
#             print("*" * 22)
#             print(f"Donor with ID {ID} has been deleted successfully.")
#             print("*" * 22)
#             print("\n")
#             break
#
#     if not donorFound:
#         print("Donor ID not found")
#
#     save_data_helper(donorData)
#
#
# def main():
#     donorData = load_data()
#
#     while True:
#         print("*" * 22)
#         print("Blood Donation System")
#         print("*" * 22)
#
#         print("1) Add Donor")
#         print("2) Search Donor")
#         print("3) Update Donor")
#         print("4) Delete Donor")
#         print("5) Exit the App")
#         choice = input("Enter your choice here: ")
#
#         match choice:
#             case '1':
#                 print("\n-----Add Donor-----\n")
#                 add_donor(donorData)
#             case '2':
#                 print("\n-----Search Donor-----\n")
#                 search_donor(donorData)
#             case '3':
#                 print("\n-----Update Donor-----\n")
#                 update_donor(donorData)
#             case '4':
#                 print("\n-----Delete Donor-----\n")
#                 delete_donor(donorData)
#             case '5':
#                 print("*" * 22)
#                 print("Have a nice day!")
#                 print("*" * 22)
#                 break
#             case _:
#                 print("*" * 22)
#                 print("Invalid Index")
#                 print("*" * 22)
#
#
# if __name__ == "__main__":
#     try:
#         main()
#     except IndexError:
#         print("*" * 22)
#         print("Invalid index")
#         print("*" * 22)
#     except ValueError:
#         print("*" * 22)
#         print("Please enter the digits")
#         print("*" * 22)




import sys
import json
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox,
    QTextEdit,
)


class BloodDonationApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Blood Donation System")
        self.resize(400, 500)
        self.setStyleSheet("background-color: #F0F0F0; font-size: 14px;")

        # Load donor data
        self.donorData = self.load_data()

        # Layout
        self.layout = QVBoxLayout()

        # Title
        self.title = QLabel("Blood Donation System")
        self.title.setStyleSheet("font-size: 20px; font-weight: bold; color: #333;")
        self.layout.addWidget(self.title)

        # Buttons
        self.add_donor_btn = QPushButton("Add Donor")
        self.add_donor_btn.setStyleSheet("background-color: #4CAF50; color: white; padding: 10px;")
        self.add_donor_btn.clicked.connect(self.show_add_donor)

        self.search_donor_btn = QPushButton("Search Donor")
        self.search_donor_btn.setStyleSheet("background-color: #2196F3; color: white; padding: 10px;")
        self.search_donor_btn.clicked.connect(self.show_search_donor)

        self.update_donor_btn = QPushButton("Update Donor")
        self.update_donor_btn.setStyleSheet("background-color: #FFC107; color: white; padding: 10px;")
        self.update_donor_btn.clicked.connect(self.show_update_donor)

        self.delete_donor_btn = QPushButton("Delete Donor")
        self.delete_donor_btn.setStyleSheet("background-color: #F44336; color: white; padding: 10px;")
        self.delete_donor_btn.clicked.connect(self.show_delete_donor)

        self.exit_btn = QPushButton("Exit")
        self.exit_btn.setStyleSheet("background-color: #9E9E9E; color: white; padding: 10px;")
        self.exit_btn.clicked.connect(self.close)

        # Add buttons to layout
        self.layout.addWidget(self.add_donor_btn)
        self.layout.addWidget(self.search_donor_btn)
        self.layout.addWidget(self.update_donor_btn)
        self.layout.addWidget(self.delete_donor_btn)
        self.layout.addWidget(self.exit_btn)

        # Output area
        self.output_area = QTextEdit()
        self.output_area.setReadOnly(True)
        self.output_area.setStyleSheet("background-color: white; padding: 10px;")
        self.layout.addWidget(self.output_area)

        self.setLayout(self.layout)

    def load_data(self):
        try:
            with open("New_Donor_Data.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_data(self):
        with open("New_Donor_Data.json", "w") as file:
            json.dump(self.donorData, file)

    def show_add_donor(self):
        self.clear_output()
        self.add_donor_window = QWidget()
        self.add_donor_window.setWindowTitle("Add Donor")
        self.add_donor_window.setStyleSheet("background-color: #F0F0F0; font-size: 14px;")

        layout = QVBoxLayout()

        # Input fields
        self.id_input = QLineEdit()
        self.id_input.setPlaceholderText("Enter 4-digit ID")
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter Name")
        self.age_input = QLineEdit()
        self.age_input.setPlaceholderText("Enter Age")
        self.cell_input = QLineEdit()
        self.cell_input.setPlaceholderText("Enter Cell Number")
        self.city_input = QLineEdit()
        self.city_input.setPlaceholderText("Enter City")
        self.blood_input = QLineEdit()
        self.blood_input.setPlaceholderText("Enter Blood Group")

        # Add fields to layout
        layout.addWidget(self.id_input)
        layout.addWidget(self.name_input)
        layout.addWidget(self.age_input)
        layout.addWidget(self.cell_input)
        layout.addWidget(self.city_input)
        layout.addWidget(self.blood_input)

        # Save button
        save_btn = QPushButton("Save Donor")
        save_btn.setStyleSheet("background-color: #4CAF50; color: white; padding: 10px;")
        save_btn.clicked.connect(self.add_donor)

        layout.addWidget(save_btn)
        self.add_donor_window.setLayout(layout)
        self.add_donor_window.show()

    def add_donor(self):
        try:
            ID = int(self.id_input.text())
            if len(str(ID)) != 4:
                QMessageBox.warning(self, "Invalid ID", "ID must be 4 digits long.")
                return

            for data in self.donorData:
                if data["id"] == ID:
                    QMessageBox.warning(self, "Duplicate ID", "Please enter a different ID.")
                    return

            name = self.name_input.text()
            age = int(self.age_input.text())
            cellNo = int(self.cell_input.text())
            city = self.city_input.text()
            bloodGroup = self.blood_input.text()

            self.donorData.append(
                {"id": ID, "name": name, "age": age, "cellNo": cellNo, "city": city, "bloodGroup": bloodGroup}
            )
            self.save_data()
            QMessageBox.information(self, "Success", "Donor data has been inserted successfully.")
            self.add_donor_window.close()
        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter valid data.")

    def show_search_donor(self):
        self.clear_output()
        self.search_donor_window = QWidget()
        self.search_donor_window.setWindowTitle("Search Donor")
        self.search_donor_window.setStyleSheet("background-color: #F0F0F0; font-size: 14px;")

        layout = QVBoxLayout()

        # Input field
        self.search_id_input = QLineEdit()
        self.search_id_input.setPlaceholderText("Enter Donor ID")

        # Search button
        search_btn = QPushButton("Search")
        search_btn.setStyleSheet("background-color: #2196F3; color: white; padding: 10px;")
        search_btn.clicked.connect(self.search_donor)

        layout.addWidget(self.search_id_input)
        layout.addWidget(search_btn)
        self.search_donor_window.setLayout(layout)
        self.search_donor_window.show()

    def search_donor(self):
        try:
            ID = int(self.search_id_input.text())
            if len(str(ID)) != 4:
                QMessageBox.warning(self, "Invalid ID", "ID must be 4 digits long.")
                return

            for data in self.donorData:
                if data["id"] == ID:
                    self.output_area.setText(
                        f"Name: {data['name']}\n"
                        f"Age: {data['age']}\n"
                        f"CellNo: 0{data['cellNo']}\n"
                        f"City: {data['city']}\n"
                        f"BloodGroup: {data['bloodGroup']}"
                    )
                    return

            QMessageBox.warning(self, "Not Found", "Donor ID not found.")
        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter a valid ID.")

    def show_update_donor(self):
        self.clear_output()
        self.update_donor_window = QWidget()
        self.update_donor_window.setWindowTitle("Update Donor")
        self.update_donor_window.setStyleSheet("background-color: #F0F0F0; font-size: 14px;")

        layout = QVBoxLayout()

        # Input fields
        self.update_id_input = QLineEdit()
        self.update_id_input.setPlaceholderText("Enter Donor ID")
        self.update_name_input = QLineEdit()
        self.update_name_input.setPlaceholderText("Enter Name")
        self.update_age_input = QLineEdit()
        self.update_age_input.setPlaceholderText("Enter Age")
        self.update_cell_input = QLineEdit()
        self.update_cell_input.setPlaceholderText("Enter Cell Number")
        self.update_city_input = QLineEdit()
        self.update_city_input.setPlaceholderText("Enter City")
        self.update_blood_input = QLineEdit()
        self.update_blood_input.setPlaceholderText("Enter Blood Group")

        # Update button
        update_btn = QPushButton("Update")
        update_btn.setStyleSheet("background-color: #FFC107; color: white; padding: 10px;")
        update_btn.clicked.connect(self.update_donor)

        layout.addWidget(self.update_id_input)
        layout.addWidget(self.update_name_input)
        layout.addWidget(self.update_age_input)
        layout.addWidget(self.update_cell_input)
        layout.addWidget(self.update_city_input)
        layout.addWidget(self.update_blood_input)
        layout.addWidget(update_btn)
        self.update_donor_window.setLayout(layout)
        self.update_donor_window.show()

    def update_donor(self):
        try:
            ID = int(self.update_id_input.text())
            if len(str(ID)) != 4:
                QMessageBox.warning(self, "Invalid ID", "ID must be 4 digits long.")
                return

            for data in self.donorData:
                if data["id"] == ID:
                    name = self.update_name_input.text()
                    age = int(self.update_age_input.text())
                    cellNo = int(self.update_cell_input.text())
                    city = self.update_city_input.text()
                    bloodGroup = self.update_blood_input.text()

                    data.update({"name": name, "age": age, "cellNo": cellNo, "city": city, "bloodGroup": bloodGroup})
                    self.save_data()
                    QMessageBox.information(self, "Success", f"Donor with ID {ID} has been updated successfully.")
                    self.update_donor_window.close()
                    return

            QMessageBox.warning(self, "Not Found", "Donor ID not found.")
        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter valid data.")

    def show_delete_donor(self):
        self.clear_output()
        self.delete_donor_window = QWidget()
        self.delete_donor_window.setWindowTitle("Delete Donor")
        self.delete_donor_window.setStyleSheet("background-color: #F0F0F0; font-size: 14px;")

        layout = QVBoxLayout()

        # Input field
        self.delete_id_input = QLineEdit()
        self.delete_id_input.setPlaceholderText("Enter Donor ID")

        # Delete button
        delete_btn = QPushButton("Delete")
        delete_btn.setStyleSheet("background-color: #F44336; color: white; padding: 10px;")
        delete_btn.clicked.connect(self.delete_donor)

        layout.addWidget(self.delete_id_input)
        layout.addWidget(delete_btn)
        self.delete_donor_window.setLayout(layout)
        self.delete_donor_window.show()

    def delete_donor(self):
        try:
            ID = int(self.delete_id_input.text())
            if len(str(ID)) != 4:
                QMessageBox.warning(self, "Invalid ID", "ID must be 4 digits long.")
                return

            for data in self.donorData:
                if data["id"] == ID:
                    self.donorData.remove(data)
                    self.save_data()
                    QMessageBox.information(self, "Success", f"Donor with ID {ID} has been deleted successfully.")
                    self.delete_donor_window.close()
                    return

            QMessageBox.warning(self, "Not Found", "Donor ID not found.")
        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter a valid ID.")

    def clear_output(self):
        self.output_area.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BloodDonationApp()
    window.show()
    sys.exit(app.exec_())
