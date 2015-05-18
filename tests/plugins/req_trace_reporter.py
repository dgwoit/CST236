from source.ReqTracer import Requirements
import logging
from nose2.events import Plugin

log = logging.getLogger('nose2.plugins.req_trace_reporter')

class ReqTraceReporter(Plugin):
    configSection = 'reqtrace'
    commandLineSwitch = (None, 'req-trace', 'Trace Requirements')

    def __init__(self):
        pass

    def startTestRun(self, event):
        pass

    def beforeErrorList(self, event):
        pass

    def beforeSummaryReport(self, event):
        pass

    def afterSummaryReport(self, event):
        f = file("reqTracer.report.txt" ,'w')
        for key in Requirements:
            log.info(key)
            f.write(key + "\r\n")
            for func in Requirements[key].func_name:
                f.write("\t" + func + "\r\n")
        f.close()
        pass