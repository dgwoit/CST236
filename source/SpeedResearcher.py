"""
:mod:`source.SpeedResearcher` -- Example source code
====================================================
"""

class SpeedDatum:
    """
    Basic speed information regarding the edge of a graph
    """
    def read(self, str_data):
        """
        Parses speed information from a line fo encoded text

        :param str_data: <city>|<city>|<distance>|<network speed>
        """
        tokens = str_data.split('|')
        self.start = tokens[0]
        self.end = tokens[1]
        self.distance = int(tokens[2])
        self.network_speed = int(tokens[3])

class SpeedData:
    """
    collection of SpeedDatums, and associated functionality
    """
    def __init__(self):
        self.data = []

    def read(self, stream):
        """
        Serializes in from stream

        :param stream: text stream
        """
        self.data = []
        for line in stream:
            record = SpeedDatum()
            record.read(line)
            self.data.append(record)

    def write(self, stream):
        """
        Serializes out to stream

        :param stream: text stream
        """
        for record in self.data:
            line = record.start
            line += '|'
            line += record.end
            line += '|'
            line += str(record.distance)
            line += '|'
            line += str(record.network_speed)
            line += '\n'
            stream.write(line)

    def find_record(self, start, end):
        """
        Finds the speed datum matching the start & end vertices

        :param start: start point (locale name)

        :param end: end point (locale name)

        :return: the matching record, otherwise None
        """
        for record in self.data:
            if record.start == start and record.end == end:
                return record

    def add(self, start, end, distance, network_speed):
        """
        Creates a speed datum from the supplied values and adds it to the collection

        :param start: start point (locale name)

        :param end: end point (locale name)

        :param distance: int

        :param network_speed: int
        """
        record = SpeedDatum()
        record.start = start
        record.end = end
        record.distance = distance
        record.network_speed = network_speed
        self.data.append(record)


class SpeedComputerPresets:
    """
    Contains user-defined values
    """
    def set_ground_speeds(self, ground_speeds):
        """
        Sets the ground speeds from ground_speeds

        :param ground_speeds:
        """
        self._ground_speeds = ground_speeds

    def get_ground_speed(self, key):
        """
        gets the ground speed matching the name of the physical transport

        :param key: string name of the physical transport

        :return: integer value of the ground speed
        """
        return self._ground_speeds[key]

    def set_start_city(self, city):
        """
        Current locality/point-of-interest (e.g. city) the user is at

        :param city: string city name
        """
        self._start_city = city

    def get_start_city(self):
        """
        :return: string
        """
        return self._start_city

    start_city = property(get_start_city, set_start_city)

class SpeedComputer:
    """
    Provides calculations of time for the movement of data along a route
    """
    def __init__(self):
        self._drive_size = 1
        self._ground_speed = 0
        self.network_latency = 0
        self.hard_drive_speed = 0

    def set_drive_size(self, drive_size):
        """
        :param drive_size: integer in GB
        """
        self._drive_size = drive_size

    def get_drive_size(self):
        """
        :return: int
        """
        return self._drive_size

    drive_size = property(get_drive_size, set_drive_size)

    def set_ground_speed(self, speed):
        """
        speed over ground for the select mode of transport

        :param speed: int/float
        """
        self._ground_speed = speed

    def get_ground_speed(self):
        """
        :return: int/float
        """
        return self._ground_speed

    transport_speed = property(get_ground_speed, set_ground_speed)
    """
    speed of the physical transport
    """

    network_latency = property()
    """
    Network latency
    """

    hard_drive_speed = property()
    """
    Hard drive speed
    """

    def calculate_drive_transport_time(self):
        """
        Calculates the drive transport time for the current leg

        :return: float
        """
        return float(self.speed_datum.distance * self.drive_size) / float(self.ground_speed)

    def calculate_drive_transport_time_from_route(self, route):
        """
        Calculates the drive transport time for a given route
        Note: set the data property before calling

        :param route: list of cities

        :return: time to traverse route
        """
        if len(route) <= 1:
            return 0
        start = route[0]
        total = 0
        if self.hard_drive_speed != 0:
            total = float(self.drive_size) / float(self.hard_drive_speed)
        print total
        for city in route:
            if city == start:
                continue
            end = city;
            print start
            print end
            self.speed_datum = self.data.find_record(start, end)
            total += self.calculate_drive_transport_time()
            print total
            start = end
        return total

    def calculate_network_transport_time_from_route(self, route):
        """
        Calculates and returns the total network transfer time for the given route

        :param route: list of cities

        :return: total data transfer time
        """
        if len(route) <= 1:
            return 0
        start = route[0]
        total = self.network_latency
        for city in route:
            if city == start:
                continue
            end = city;
            print start
            print end
            self.speed_datum = self.data.find_record(start, end)
            total += self.calculate_network_transport_time()
            start = end
        return total

    def calculate_network_transport_time(self):
        """
        Calculates and returns the network transport time for the data for a given leg of a route

        :return: time
        """
        return float(self.drive_size) / float(self.speed_datum.network_speed)

    def calculate_transport_time_difference(self):
        """
        Returns the time difference between using the physical transport for data and the network transport for data

        :return: time
        """
        return self.calculate_drive_transport_time() - self.calculate_network_transport_time()

