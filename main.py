from flight import DomesticFlight, InternationalFlight
from airline import Airline
from booking import Booking

def main():
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
    booking1 = Booking("Minta Károly", flight1)
    booking2 = Booking("Példa József", flight2)
    booking3 = Booking("Ismert Kata", flight3)
    booking4 = Booking("Kiss András", flight1)
    booking5 = Booking("Senki Bercel", flight2)
    booking6 = Booking("Minden Elemér", flight3)

    # Foglalások hozzáadása a
    airline.add_booking(booking1)
    airline.add_booking(booking2)
    airline.add_booking(booking3)
    airline.add_booking(booking4)
    airline.add_booking(booking5)
    airline.add_booking(booking6)

    while True:
        print("\nKérem válasszon a lenti menüből: ")
        print("[A] Jegy foglalása: ")
        print("[B] Foglalás lemondása: ")
        print("[C] Foglalások listázása: ")
        print("[X] Kilépés")

        choice = input("> ").lower()

        if choice == "a":
            airline.book_flight()
        elif choice == "b":
            airline.cancel_booking()
        elif choice == "c":
            airline.list_bookings()
        elif choice == "x":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()