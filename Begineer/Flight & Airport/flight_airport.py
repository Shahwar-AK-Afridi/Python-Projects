class Flight():

    def __init__(self, number, departure_date, departure_time, departure_airport, arrival_airport) -> None:
        self.number = number
        self.departure_date = departure_date
        self.departure_time = departure_time
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport


class Airport():

    def __init__(self, name, code) -> None:
        self.name = name
        self.code = code

    def __str__(self):
        representation = "Airport:{} & Code:{}".format(self.name, self.code)
        return representation