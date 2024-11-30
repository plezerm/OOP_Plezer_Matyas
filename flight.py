from abc import ABC, abstractmethod

# Ős repülőjárat

class Flight(ABC):
    def __init__(self, flight_number, destination, price):
        self.flight_number = flight_number
        self.destination = destination
        self.price = price

    @abstractmethod
    def __str__(self):
        pass

# Belföldi Járat

class DomesticFlight(Flight):
    def __init__(self, flight_number, destination, price):
        super().__init__(flight_number, destination, price)

    def __str__(self):
        return f"Belföldi Járat {self.flight_number}: {self.destination} - {self.price} Ft"


# Nemzetközi Járat

class InternationalFlight(Flight):
    def __init__(self, flight_number, destination, price):
        super().__init__(flight_number, destination, price)

    def __str__(self):
        return f"Nemzetközi Járat {self.flight_number}: {self.destination} - {self.price} Ft"