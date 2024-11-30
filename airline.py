from booking import Booking

#légitársaság osztály
class Airline:
    def __init__(self, name):
        self.name = name
        self.__flights = []
        self.__bookings = []

#Járat hozzádása

    def add_flight(self, flight):
        self.__flights.append(flight)

#foglalás hozzáadása

    def add_booking(self, booking):
        self.__bookings.append(booking)

#Járatok listázása

    def list_flights(slef):
        print("Elérhető Járatok: ")
        for i, flight in enumerate(self.__flights):
            print(f"{i+1}. {flight}")

#Járat foglalása

def book_flight(self):
        self.list_flights()
        try:
            choice = int(input("Kérem válaszz járat számod: ")) - 1
            flight = self.__flights[choice]
            passenger_name = input("Utas neve: : ")
            booking = Booking(passenger_name, flight)
            self.__bookings.append(booking)
            print(f"Sikeres foglalás! Végösszeg: {flight.price} Ft")
        except (ValueError, IndexError):
            print("Nincs ilyen járat! ")

