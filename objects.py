class Client:
    def __init__(self, name, contact, client_id):
        # Constructor for the Client class
        self.name = name
        self.contact = contact
        self.client_id = client_id


class Vehicle:
    def __init__(self, plate, model, year, vehicle_type, one_day_rental):
        # Constructor for the Vehicle class
        self.plate = plate
        self.model = model
        self.year = year
        self.vehicle_type = vehicle_type
        self.one_day_rental = one_day_rental
        self.availability = True

    def check_availability(self) -> str:
        # checks if the vehicle is available for rent
        return "Available" if self.availability else "Unavailable"

    def __str__(self) -> str:
        # displays information about the vehicle
        return f"Plate: {self.plate}, Model: {self.model}, Year: {self.year}, Type: {self.vehicle_type}, Availability: {'yes' if self.availability else 'no'}, one day rental: {self.one_day_rental} bucks"


class Car(Vehicle):
    def __str__(self) -> str:
        return f"Car - {super().__str__()}"


class Bike(Vehicle):
    def __str__(self) -> str:
        return f"Bike - {super().__str__()}"


class Reservation:
    def __init__(self, reservation_id, client_id, vehicle, rental_date, return_date):
        # Constructor for the Reservation class
        self.reservation_id = reservation_id
        self.client_id = client_id
        self.vehicle = vehicle
        self.rental_date = rental_date
        self.return_date = return_date
        self.cost = self.calculate_cost()

    def calculate_cost(self):
        # Placeholder for calculating the cost of the reservation
        rental_days = (self.return_date - self.rental_date).days
        cost = rental_days * self.vehicle.one_day_rental
        return cost

    def confirm_reservation(self):
        try:
            with open("reservations.csv", "at") as history:
                history.write(
                    f"{self.reservation_id},{self.client_id},{self.vehicle.plate},"
                    f"{self.rental_date},{self.return_date},{self.cost}\n"
                )
            return f"Reservation number {self.reservation_id} is done. Thanks for choosing us."
        except Exception as e:
            print(f"Something wrong happened: {e}")

    def cancel_reservation(self):
        # Placeholder for canceling a reservation
        with open("reservations.csv", "rt") as archive:
            lines = [line for line in archive]
