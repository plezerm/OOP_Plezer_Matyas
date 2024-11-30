# Az utas neve, aki a foglalást végzi és A járat, amire a foglalás vonatkozik.
class Booking:
    def __init__(self, passenger_name, flight):
        self.passenger_name = passenger_name
        self.flight = flight

    def __str__(self):
        return f"{self.passenger_name} -> {self.flight}"