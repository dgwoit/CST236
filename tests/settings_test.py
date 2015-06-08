from unittest import TestCase
from settings import *
from StringIO import StringIO
import json

class TestSettings(TestCase):
    def setUp(self):
        self.settings = Settings()

    def tearDown(self):
        pass

    def test_arrival_radius_default(self):
        assert self.settings.arrival_radius > 0

    def test_global_settings(self):
        global settings
        self.assertIsNotNone(settings)

    def test_settings_serialization(self):
        self.settings.arrival_radius = 1234.5

        #verify serializabiliity
        fout = StringIO()
        json.dump(self.settings.encode(), fout)
        text_data = fout.getvalue()

        #serialize back in and test
        fin = StringIO(text_data)
        data = json.load(fin)
        decoded_settings = Settings.decode(data)
        assert decoded_settings.arrival_radius == self.settings.arrival_radius
