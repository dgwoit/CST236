"""
Speed Researcher
"""

class SpeedDatum:
    def read(self, str_data):
        tokens = str_data.split('|')
        self.start = tokens[0]
        self.end = tokens[1]
        self.distance = int(tokens[2])
        self.network_speed = int(tokens[3])

class SpeedData:
    def read(self, stream):
        self.data = []
        for line in stream:
            record = SpeedDatum()
            record.read(line)
            self.data.append(record)

    def find_record(self, start, end):
        for record in self.data:
            if record.start == start and record.end == end:
                return record

class SpeedComputer:
    def __init__(self):
        self._drive_size = 1
        self._ground_speed = 0

    def set_drive_size(self, drive_size):
        self._drive_size = drive_size

    def get_drive_size(self):
        return self._drive_size

    drive_size = property(get_drive_size, set_drive_size)

    def set_ground_speed(self, speed):
        self._ground_speed = speed

    def get_ground_speed(self):
        return self._ground_speed

    transport_speed = property(get_ground_speed, set_ground_speed)

    def calculate_drive_transport_time(self):
        return float(self.speed_datum.distance * self.drive_size) / float(self.ground_speed)

    def calculate_network_transport_time(self):
        return float(self.drive_size) / float(self.speed_datum.network_speed)

    def calculate_transport_time_difference(self):
        return self.calculate_drive_transport_time() - self.calculate_network_transport_time()

