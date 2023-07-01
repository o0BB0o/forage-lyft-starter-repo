from battery import Battery


class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        next_service_date = self.last_service_date.replace(self.last_service_date.year + 2)
        if next_service_date < self.current_date:
            return True
        else:
            return False