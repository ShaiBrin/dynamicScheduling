class Service:
    def __init__(self, service_id, service_name, description):
        self.service_id = service_id
        self.service_name = service_name
        self.description = description

    def __repr__(self):
        return f"Service({self.service_name})"