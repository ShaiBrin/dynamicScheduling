class Maid:
    def __init__(self, maid_id, name, location, services_available, rating, phone, email):
        self.maid_id = maid_id
        self.name = name
        self.location = location.split(",")  # List of locations
        self.services_available = services_available.split(",")  # List of services
        self.rating = rating
        self.phone = phone
        self.email = email

    def __repr__(self):
        return f"Maid({self.name}, {self.location}, Services: {self.services_available})"