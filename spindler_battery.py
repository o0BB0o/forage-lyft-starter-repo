from battery import Battery


class SpindlerBattery(Battery):
    def __init__(self, curr_date, last_date):
        self.curr_date = curr_date
        self.last_date = last_date

    def needs_service(self):
        next_date = self.last_date.replace(self.last_date.year + 3)
        if next_date < self.curr_date:
            return True
        else:
            return False
