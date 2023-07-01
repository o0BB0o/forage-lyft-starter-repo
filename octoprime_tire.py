from tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        total_sum = sum(self.tirewear)
        return total_sum >= 3.0