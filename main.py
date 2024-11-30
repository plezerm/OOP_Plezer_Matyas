from flight import DomesticFlight, InternationalFlight
from airline import Airline
from booking import Booking

def main()
    # Légitársaság létrehozása
    airline = Airline("Malév")

    # Járatok létrehozása
    flight1 = DomesticFlight("M5 554", "Budapest", 13000)
    flight2 = InternationalFlight("M9 111", "Berlin", 49000)
