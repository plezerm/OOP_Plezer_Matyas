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

