from engine import Engine


class WilloughbyEngine(Engine):
    def __init__(self, curr_mileage, last_mileage):
        self.curr_mileage = curr_mileage
        self.last_mileage = last_mileage

    def needs_service(self):
        return self.curr_mileage - self.last_mileage > 60000
