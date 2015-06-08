import math

class LatLon:
    def __init__(self, lat=0, lon=0):
        self.lat = 0
        self.lon = 0
        self.setLat(lat)
        self.setLon(lon)

    def getLat(self):
        return self.lat

    def setLat(self, value):
        if value > 90:
            raise Exception
        if value < -90:
            raise Exception
        self.lat = value

    def getLon(self):
        return self.lon

    def setLon(self, value):
        #normalize if out of range
        if value <= -180 or value > 180:
            value = ((value + 180) % 360) - 180
        self.lon = value

    Lat = property(getLat, setLat)
    Lon = property(getLon, setLon)

    #rhumb line distance
    def distance(self, dest_ll):
        #rhumb line distance
        R = 6371000  # metres
        phi1 = math.radians(self.getLat())
        phi2 = math.radians(dest_ll.getLat())
        delta_phi = math.radians(dest_ll.getLat()-self.getLat())
        delta_psi = math.log(math.tan(math.pi/4+phi2/2)/math.tan(math.pi/4+phi1/2))
        delta_lambda = math.radians(dest_ll.getLon()-self.getLon())
        q = 0
        if abs(delta_psi) > 10e-12:
            q = delta_phi/delta_psi
        else:
            q = math.cos(phi1)

        dist = math.sqrt(delta_phi*delta_phi + q*q*delta_lambda*delta_lambda) * R
        return dist

        #great circle distance
        """
        R = 6371000 # metres
        phi1 = math.radians(self.getLat())
        phi2 = math.radians(rhll.getLat())
        delta_phi = math.radians(rhll.getLat()-self.getLat())
        delta_lambda = math.radians(rhll.getLon()-self.getLon())

        a = math.sin(delta_phi/2) * math.sin(delta_phi/2) +\
                math.cos(phi1) * math.cos(phi2) *\
                math.sin(delta_lambda/2) * math.sin(delta_lambda/2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        d = R * c

        return d
        """

    def project(self, bearing, distance):
        R = 6371000  # metres
        delta = distance / R
        theta = math.radians(bearing)
        delta_phi = delta*math.cos(theta)
        phi1 = math.radians(self.getLat())
        lambda1 = math.radians(self.getLon())
        phi2 = phi1 + delta_phi
        delta_psi = math.log(math.tan(phi2/2+math.pi/4)/math.tan(phi1/2+math.pi/4))
        q = 0
        if delta_psi > 10e-12:
            q = delta_phi / delta_psi
        else:
            q = math.cos(phi1)
        delta_lambda = delta*math.sin(theta)/q

        lambda2 = (lambda1+delta_lambda+math.pi) % (2*math.pi) - math.pi
        return LatLon(math.degrees(phi2), math.degrees(lambda2))

    def encode(self):
        return {"lat": self.getLat(), "lon": self.getLon()}

    @staticmethod
    def decode(data):
        return LatLon(data['lat'], data['lon'])