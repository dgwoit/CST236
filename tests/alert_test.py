__author__ = 'drock'

import logging
from unittest import TestCase
import StringIO

class TestAlerts(TestCase):
    #from http://stackoverflow.com/questions/9534245/python-logging-to-stringio-handler
    def setUp(self):
        self.stream = StringIO.StringIO()
        self.handler = logging.StreamHandler(self.stream)
        self.stream_module_a = StringIO.StringIO()
        self.handler_module_a = logging.StreamHandler(self.stream)
        self.stream_module_b = StringIO.StringIO()
        self.handler_module_b = logging.StreamHandler(self.stream)
        self.log = logging.getLogger('modules')
        #self.log.setLevel(logging.INFO)
        for handler in self.log.handlers:
            self.log.removeHandler(handler)
        self.log.addHandler(self.handler)
        self.log_module_a = logging.getLogger('modules.a')
        for handler in self.log_module_a.handlers:
            self.log_module_a.removeHandler(handler)
        self.log_module_a.addHandler(self.handler_module_a)
        self.log_module_b = logging.getLogger('modules.b')
        for handler in self.log_module_b.handlers:
            self.log_module_b.removeHandler(handler)
        self.log_module_b.addHandler(self.handler_module_b)


    def configure_log(self, level, module):
        return

    #frome http://stackoverflow.com/questions/9534245/python-logging-to-stringio-handler
    def test_module_a_log(self):
        self.log.setLevel(logging.DEBUG)
        logger = logging.getLogger('modules.a');
        logger.info('a')
        print '[', self.stream.getvalue(), ']'
        self.assertTrue(self.stream.getvalue(), 'a')

    def test_module_b_log(self):
        self.setUp()
        self.log.setLevel(logging.DEBUG)
        #self.handler.flush()
        logger = logging.getLogger('modules.b')
        logger.info('b')
        print '[', self.stream.getvalue(), ']'
        self.assertTrue(self.stream.getvalue(), 'b')
        self.tearDown()

    def test_all_modules_log_module_a(self):
        self.log.setLevel(logging.DEBUG)
        self.stream.flush()
        logging.getLogger('modules.a').log('a')
        self.handler_module_a.flush()
        print '[', self.stream.getvalue(), ']'
        self.assertTrue(self.stream.getvalue(), 'a')

    def test_all_modules_log_module_b(self):
        self.log.setLevel(logging.DEBUG)
        logging.getLogger('modules.b').info('b');
        print '[', self.stream.getvalue(), ']'
        self.assertTrue(self.stream.getvalue(), 'b')

    def test_all_modules_log_level_critical(self):
        logger = logging.getLogger('modules')
        logging.setLevel(logging.CRITICAL)
        logging.getLogger('modules.a').critical('critical');
        print '[', self.stream.getvalue(), ']'
        self.assertTrue(self.stream.getvalue(), 'critical')

    def test_all_modules_log_level_not_critical(self):
        #self.log.info("test")
        #self.handler.flush()
        logger = logging.getLogger('modules')
        logger.setLevel(logging.CRITICAL)
        logging.getLogger('modules.a').debug('debug');
        print '[', self.stream.getvalue(), ']'
        self.assertTrue(self.stream.getvalue(), '')

    #from http://stackoverflow.com/questions/9534245/python-logging-to-stringio-handler
    def tearDown(self):
        self.log.removeHandler(self.handler)
        self.handler.close()
        self.log.removeHandler(self.handler_module_a)
        self.handler_modules_a.close()
        self.log.removeHandler(self.handler_module_b)
        self.handler_modules_b.close()

