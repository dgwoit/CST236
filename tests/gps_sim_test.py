from unittest import TestCase
from gps_simulator import GPSSimulator
from mock import patch
import threading
import re

class TestGPSSimulator(TestCase):
    def setUp(self):
        self.simulator = GPSSimulator()
        self.simulator.speed_over_ground = 5.0
        self.track_angle_true = 45

    def tearDown(self):
        self.simulator = None


    gps_sentence = None

    def test_RMC_generation(self):
        real_generator = self.simulator.generate_rmc_sentence
        with patch("gps_simulator.GPSSimulator.generate_rmc_sentence") as mock:
            event = threading.Event()
            gps_sentence = None
            def my_generate_rmc():
                print "my_generate_rmc"
                TestGPSSimulator.gps_sentence = real_generator()
                print TestGPSSimulator.gps_sentence
                event.set()
                return TestGPSSimulator.gps_sentence
            mock.side_effect = my_generate_rmc
            self.simulator.start()
            event.wait(10.00)
            self.simulator.stop()
            self.assert_valid_sentence(TestGPSSimulator.gps_sentence,
                                       "RMC,\d{6},[AV],\d+\.\d+,[NS],\d+\.\d+,[EW],\d+\.\d,\d+\.[0-9],\d{8},\d+.[0-9],[EW]"
                                       )

    def test_GLL_generation(self):
        real_generator = self.simulator.generate_gll_sentence
        with patch("gps_simulator.GPSSimulator.generate_gll_sentence") as mock:
            event = threading.Event()
            TestGPSSimulator.gps_sentence = None
            def my_generate_gll():
                print "my_generate_gll"
                TestGPSSimulator.gps_sentence = real_generator()
                print TestGPSSimulator.gps_sentence
                event.set()
                return TestGPSSimulator.gps_sentence
            mock.side_effect = my_generate_gll
            self.simulator.start()
            event.wait(10.00)
            self.simulator.stop()
            self.assert_valid_sentence(TestGPSSimulator.gps_sentence,
                                       "GLL,\d+\.\d+,[NS],\d+\.\d+,[EW],[0-9]{6},[AV]"
                                       )

    def assert_valid_sentence(self, sentence, sub_pattern):
        pattern = "\$GP" + sub_pattern # + "(,\*[0-9A-F]{2}|)"
        self.assertIsNotNone(sentence)
        compiled_pattern = re.compile(pattern)
        result = compiled_pattern.match(sentence)
        self.assertIsNotNone(result, "no match for '%s'" % pattern)

