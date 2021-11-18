class Elevators:
    Time = 0

    def __init__(self, d: dict):
        self.id = d.get("_id")
        self.speed = d.get("_speed")
        self.min_floor = d.get("_minFloor")
        self.max_floor = d.get("_maxFloor")
        self.close_time = d.get("_closeTime")
        self.open_time = d.get("_openTime")
        self.start_time = d.get("_startTime")
        self.stop_time = d.get("_stopTime")

    def time(self, src, des):
        df = des - src
        return self.close_time + self.start_time + df / self.speed + self.stop_time + self.open_time
