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

    def list_flights(self):
        print("Elérhető járatok:")
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

#Járat törlése

    def cancel_booking(self):
        print("Jelenlegi foglalások:")
        for i, booking in enumerate(self.__bookings):
            print(f"{i+1}. {booking}")
        try:
            choice = int(input("Kérem válassza ki a törölni kívánt foglalást: ")) - 1
            del self.__bookings[choice]
            print("Foglalás sikeresen törölve lett!")
        except (ValueError, IndexError):
            print("Nincs ilyen foglalás!")

# Járatok listázása

    def list_bookings(self):
        print("Jelenlegi foglalások:")
        if self.__bookings:
            for booking in self.__bookings:
                print(booking)
        else:
            print("Nincsenek foglalások.")   

# name attribútumának értéke

    def __str__(self):
        return f"{self.name} airline"
