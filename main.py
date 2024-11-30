from flight import DomesticFlight, InternationalFlight
from airline import Airline
from booking import Booking

def main()
    # Légitársaság létrehozása
    airline = Airline("Malév")

    # Járatok létrehozása
    flight1 = DomesticFlight("M5 554", "Budapest", 13000)
    flight2 = InternationalFlight("M9 111", "Berlin", 49000)
    flight3 = InternationalFlight("M9 999", "Pozsony", 35000)

    # Járatok hozzárendelése a légitársasághoz

    airline.add_flight(flight1)
    airline.add_flight(flight2)
    airline.add_flight(flight3)

    # Foglalások létrehozása



    # Foglalások hozzáadása 
    