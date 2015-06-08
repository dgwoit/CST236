


class Settings:
    def __init__(self):
        self.arrival_radius = 100

    def encode(self):
        return {"arrival_radius": self.arrival_radius}

    @staticmethod
    def decode(data):
        instance = Settings()
        instance.arrival_radius = float(data["arrival_radius"])
        return instance

settings = Settings()

