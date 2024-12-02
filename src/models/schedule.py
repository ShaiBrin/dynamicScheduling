class Schedule:
    def __init__(self, maid_id, date, start_time, end_time):
        self.maid_id = maid_id
        self.date = date
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return f"Schedule(Maid: {self.maid_id}, Date: {self.date}, Time: {self.start_time}-{self.end_time})"
