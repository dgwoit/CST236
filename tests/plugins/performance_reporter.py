from source.PerformanceDecorator import PerformanceFuncs
from nose2.events import Plugin
import time
import logging

logger = logging.getLogger(__file__)

class PerformanceReporter(Plugin):
    configSection = 'performance'
    commandLineSwitch = (None, 'performance', 'Record Performance')

    def __init__(self):
        self.start_time = None
        self.run_times = {}

    def startTest(self, event):
        self.start_time = time.clock()

    def stopTest(self, event):
        duration = time.clock() - self.start_time
        self.run_times[event.test] = duration

    def afterSummaryReport(self, event):
        f = file("performance.report.txt" ,'w')
        f.write("test case, duration\n")
        for key in self.run_times:
            fname = str(key).split()[0]
            if fname not in PerformanceFuncs:
                continue
            logger.info(key)
            line = "{0}, {1}\n".format(fname, str(self.run_times[key]))
            f.write(line)
        f.close()

