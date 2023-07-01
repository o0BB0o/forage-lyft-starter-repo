from engine import Engine


class CapuletEngine(Engine):
    def __init__(self, curr_milage, last_mileage):
        self.curr_milage = curr_milage
        self.last_mileage = last_mileage

    def needs_service(self):
        return self.curr_milage - self.last_mileage > 30000
