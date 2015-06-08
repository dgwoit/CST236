import threading
import time
from latlon import LatLon
import datetime


class GPSSimulator(threading.Thread):
    def __init__(self):
        super(GPSSimulator, self).__init__()
        self.stop_event = threading.Event()
        self.position = LatLon()
        self.speed_over_ground = 0
        self.track_angle_true = 0
        self.magnetic_variation = 0
        self.fn_send = None

    def run(self):
        then = time.clock()
        while self.stop_event.isSet()==False:
            time.sleep(1.0)
            now = time.clock()
            time_elapsed = now-then
            then = now
            distance = self.speed_over_ground * time_elapsed
            self.position = self.position.project(self.track_angle_true, time_elapsed)
            self.emit_sentence(self.generate_rmc_sentence())
            self.emit_sentence(self.generate_gll_sentence())


    def stop(self):
        self.stop_event.set()
        self.join()

    def emit_sentence(self, sentence):
        pass

    def generate_rmc_sentence(self):
        print "generate_rmc_sentence"
        return "$GPRMC,{0},A,{1},{2},{3},{4},{5}".format(self.nmea_utc(), self.nmea_latlon(), self.nmea_speed_over_ground(),\
            self.nmea_track_angle(), self.nmea_date(), self.nmea_magnetic_variation())

    def generate_gll_sentence(self):
        print "generate_gll_sentence"
        return "$GPGLL,{0},{1},A".format(self.nmea_latlon(), self.nmea_utc())

    def nmea_utc(self):
        #t = datetime.datetime(time.gmtime())
        t = datetime.datetime.utcnow()
        return t.strftime("%H%M%S")

    def nmea_date(self):
        return datetime.datetime.utcnow().strftime("%Y%m%d")

    def nmea_latlon(self):
        lat_degrees = int(abs(self.position.lat))
        lat_minutes = 60.0 * (abs(self.position.lat) - lat_degrees)
        lat_decimal_minutes = int(1000.0 * (lat_minutes - int(lat_minutes)))
        lat_minutes = int(lat_minutes)
        ns_mark = "N"
        lon_degrees = int(abs(self.position.lon))
        lon_minutes = 60.0 * (abs(self.position.lon) - lon_degrees)
        lon_decimal_minutes = int(1000.0 * (lon_minutes) - int(lon_minutes))
        lon_minutes = int(lon_minutes)
        ew_mark = "E"
        return "%03d%02d.%03d,%s,%03d%02d.%03d,%s" % (lat_degrees, lat_minutes, lat_decimal_minutes, ns_mark,
                                                   lon_degrees, lon_minutes, lon_decimal_minutes, ew_mark)

    def nmea_speed_over_ground(self):
        return "%03.1f" % (1.94384 * self.speed_over_ground)

    def nmea_track_angle(self):
        return "%03.1f" % self.track_angle_true

    def nmea_magnetic_variation(self):
        abs_mag_var = abs(self.magnetic_variation)
        ew_mark = "W"
        return "%03.1f,%s" % (abs_mag_var, ew_mark)