# Blood Donation System

import json


def load_data():

    try:
        with open('New_Donor_Data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_data_helper(donorData):

    with open('New_Donor_Data.json', 'w') as file:
        json.dump(donorData, file)


def is_valid_id(ID):

    if len(str(ID)) != 4:
        print("*" * 22)
        print("Invalid ID: ID must be 4 digits long.")
        print("*" * 22)
        return exit()


def is_digit(*args):

    arg = ''.join(str(arg) for arg in args)
    if arg.isdigit():
        print("*" * 22)
        print("Invalid Index")
        print("*" * 22)
        return exit()


def is_duplicate(donorData, ID):

    for data in donorData:
        if data['id'] == ID:
            print("*" * 22)
            print("Please enter the different ID.")
            print("*" * 22)
            return exit()


def add_donor(donorData):

    ID = int(input("Enter 4 digits ID: "))
    is_valid_id(ID)
    is_duplicate(donorData, ID)

    name = input("Enter Name: ")
    is_digit(name)

    age = int(input("Enter Age: "))
    cellNo = int(input("Enter CellNo: "))
    city = input("Enter City: ")
    is_digit(city)

    bloodGroup = input("Enter BloodGroup: ")
    is_digit(bloodGroup)

    print("*" * 22)
    print(f"Donor data has been inserted successfully.")
    print("*" * 22)
    print("\n")

    donorData.append({'id': ID, 'name': name, 'age': age, 'cellNo': cellNo, 'city': city, 'bloodGroup': bloodGroup})
    save_data_helper(donorData)


def search_donor(donorData):

    ID = int(input("Enter Donor ID: "))
    is_valid_id(ID)

    for data in donorData:
        if data['id'] == ID:
            print(f"Name: {data['name']}")
            print(f"Age: {data['age']}")
            print(f"CellNo: 0{data['cellNo']}")
            print(f"City: {data['city']}")
            print(f"BloodGroup: {data['bloodGroup']}")
            print("\n")
            return []
    print("ID not found.")
    return exit()


def update_donor(donorData):

    ID = int(input("Enter Donor ID: "))
    is_valid_id(ID)

    for data in donorData:
        if data['id'] == ID:
            ID = int(input("Enter new 4 digits ID: "))
            is_valid_id(ID)

            name = input("Enter Name: ")
            is_digit(name)

            age = int(input("Enter Age: "))
            cellNo = int(input("Enter CellNo: "))
            city = input("Enter City: ")
            is_digit(city)

            bloodGroup = input("Enter BloodGroup: ")
            is_digit(bloodGroup)

            print("*" * 22)
            print(f"Donor with ID {ID} has been updated successfully.")
            print("*" * 22)
            print("\n")

            data.update({'id': ID, 'name': name, 'age': age, 'cellNo': cellNo, 'city': city, 'bloodGroup': bloodGroup})
            save_data_helper(donorData)


def delete_donor(donorData):

    ID = int(input("Enter Donor ID: "))
    is_valid_id(ID)

    donorFound = False

    for data in donorData:
        if data['id'] == ID:
            donorData.remove(data)
            donorFound = True
            print("*" * 22)
            print(f"Donor with ID {ID} has been deleted successfully.")
            print("*" * 22)
            print("\n")
            break

    if not donorFound:
        print("Donor ID not found")

    save_data_helper(donorData)


def main():
    donorData = load_data()

    while True:
        print("*" * 22)
        print("Blood Donation System")
        print("*" * 22)

        print("1) Add Donor")
        print("2) Search Donor")
        print("3) Update Donor")
        print("4) Delete Donor")
        print("5) Exit the App")
        choice = input("Enter your choice here: ")

        match choice:
            case '1':
                print("\n-----Add Donor-----\n")
                add_donor(donorData)
            case '2':
                print("\n-----Search Donor-----\n")
                search_donor(donorData)
            case '3':
                print("\n-----Update Donor-----\n")
                update_donor(donorData)
            case '4':
                print("\n-----Delete Donor-----\n")
                delete_donor(donorData)
            case '5':
                print("*" * 22)
                print("Have a nice day!")
                print("*" * 22)
                break
            case _:
                print("*" * 22)
                print("Invalid Index")
                print("*" * 22)


if __name__ == "__main__":
    try:
        main()
    except IndexError:
        print("*" * 22)
        print("Invalid index")
        print("*" * 22)
    except ValueError:
        print("*" * 22)
        print("Please enter the digits")
        print("*" * 22)
