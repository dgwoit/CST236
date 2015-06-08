from threading import Thread, Event
from vessel import Vessel
import time

class DeadReckoner(Thread):
    def __init__(self, vessel, *args, **kwargs):
        super(DeadReckoner, self).__init__(*args, **kwargs)
        self.vessel = vessel
        self.stop_event = Event()

    def run(self):
        then = time.clock()
        while not self.stop_event.isSet():
            time.sleep(1.0)
            now = time.clock()
            self.simulate(now-then)
            then = now

    def stop(self):
        self.stop_event.set();
        self.join()

    def simulate(self, delta_t):
        distance = self.vessel.speed_over_ground * delta_t
        position = self.vessel.position.project(self.vessel.heading_true, distance)
        self.vessel.position = position

