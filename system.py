import objects as obj
import os


def clear_screen():
    # Function to clear the console screen
    os.system("clear" if os.name == "posix" else "cls")


def clear_menu():
    # Function to clear screen between choices
    input("Press Enter to continue: ")
    clear_screen()


clear_screen()


class VehicleRentalSystem:
    def __init__(self):
        self.employees = []
        self.clients = []
        self.vehicles = []
        self.reservations = []

    def display_menu(self):
        # Display the main menu
        print("\nVehicle Rental System Menu:")
        print("1. Add Employee")
        print("2. Add Client")
        print("3. Add Vehicle")
        print("4. Make Reservation")
        print("5. Display Vehicle Information")
        print("6. Show Vehicle Catalog")
        print("7. Exit")

    def add_employee(self):
        # Function to add an employee to the system
        name = input("Enter employee name: ")
        contact = input("Enter employee contact information: ")
        emp_id = input("Enter employee ID: ")
        commission_rate = float(input("Enter employee commission rate: "))
        new_employee = obj.Employee(name, contact, emp_id, commission_rate)
        self.employees.append(new_employee)

    def add_client(self):
        # Function to add a client to the system
        name = input("Enter client name: ")
        contact = input("Enter client contact information: ")
        client_id = input("Enter client ID: ")
        new_client = obj.Client(name, contact, client_id)
        self.clients.append(new_client)

    def add_vehicle(self):
        # Function to add a vehicle to the system
        plate = input("Enter vehicle plate: ")
        model = input("Enter vehicle model: ")
        year = input("Enter vehicle year: ")
        vehicle_type = input("Enter vehicle type: ")
        new_vehicle = obj.Vehicle(plate, model, year, vehicle_type)
        self.vehicles.append(new_vehicle)

    def make_reservation(self):
        # Function to make a reservation
        client_id = input("Enter client ID: ")
        emp_id = input("Enter employee ID: ")
        vehicle_plate = input("Enter vehicle plate for reservation: ")
        rental_date = input("Enter rental date: ")
        return_date = input("Enter return date: ")
        new_reservation = obj.Reservation(
            len(self.reservations) + 1,
            client_id,
            emp_id,
            vehicle_plate,
            rental_date,
            return_date,
        )
        self.reservations.append(new_reservation)
        print(f"Reservation {new_reservation.reservation_id} created successfully!")

    def display_vehicle_information(self):
        # Function to display information about a vehicle
        vehicle_plate = input("Enter vehicle plate: ")
        found_vehicle = next(
            (vehicle for vehicle in self.vehicles if vehicle.plate == vehicle_plate),
            None,
        )
        if found_vehicle:
            print(found_vehicle.show_info())
        else:
            print("Vehicle not found.")

    def show_vehicle_catalog(self):
        # Function to display all vehicles in the system
        print("\nVehicle Catalog:")
        for vehicle in self.vehicles:
            print(vehicle.show_info())
            input("Press Enter to continue: ")
            clear_screen()

    def run(self):
        # Main function to run the system
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-7): ")
            if choice == "1":
                self.add_employee()

            elif choice == "2":
                self.add_client()

            elif choice == "3":
                self.add_vehicle()

            elif choice == "4":
                self.make_reservation()

            elif choice == "5":
                self.display_vehicle_information()

            elif choice == "6":
                self.show_vehicle_catalog()

            elif choice == "7":
                print("Exiting Vehicle Rental System. Goodbye!")
                clear_menu()
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 7.")
            clear_menu()


if __name__ == "__main__":
    clear_screen()
    vehicle_rental_system = VehicleRentalSystem()
    vehicle_rental_system.run()
