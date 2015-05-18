from unittest import TestCase
from pywinauto import application, win32defines, controls, clipboard, handleprops
import logging
import time
import ctypes
from source.ReqTracer import *

logger = logging.getLogger(__file__)

class TestSharpTona(TestCase):
    question_box_id = u'WindowsForms10EDITapp02bf8098_r13_ad12'
    answer_box_id = u'WindowsForms10EDITapp02bf8098_r13_ad13'
    correct_button_id = u'Correct'
    teach_button_id = u'Teach'

    def setUp(self):
        self.app = application.Application()
        self.app.start_("target/sharpTona.exe", 30)
        self.sharpTona = self.app.sharpTona
        self.correct_button = self.sharpTona[self.correct_button_id]
        self.teach_button = self.sharpTona[self.teach_button_id]
        self.question_box = self.sharpTona[self.question_box_id]
        self.answer_box = self.sharpTona[self.answer_box_id]

    def tearDown(self):
        self.app.sharpTona.TypeKeys('%{F4}')


    def inspect_label(self, control_name, expected_text):
        control = self.app.SharpTona[control_name]
        self.assertIsNotNone(control, control_name + " control not found")
        logger.info(control.Class)
        self.assertRegexpMatches(control.Class, '.*STATIC.*', "not a static control")
        logger.info("'{0}'".format(control.Text))
        self.assertRegexpMatches(control.Text, expected_text, "field does not contain '{0}'".format(expected_text))

    ### Assert Methods ###

    def assertTextEqual(self, lh_val, rh_val):
        assert lh_val == rh_val, "'{0}' does not match '{1}'".format(lh_val, rh_val)

    def assertControlDisabled(self, c):
        control = None
        control_name = None
        if c is str:
            control_name = c
            control = self.app.sharpTona[control_name];
        else:
            control_name = c.Text
            control = c
        logger.info(control)
        logger.info(control.Class)
        assert control.IsEnabled == False, "Control '{0}' is not disabled".format(control_name)

    def assertControlEnabled(self, value):
        control_name = None
        control = None
        if value is str:
            control_name = value
            control = self.app.sharpTona[control_name];
        else:
            control = value
            control_name = self.get_control_text(control)
        logger.info(control)
        logger.info(control.Class)
        assert control.IsEnabled == True, "Control '{0}' is not enabled".format(control_name)

    def assertControlVisible(self, control):
        logger.info(control)
        logger.info(control.Class)
        assert control.IsVisible == True, "Control '{0}' is not visible".format(control)


    ### Helper Methods ###

    def set_control_text(self, control, text):
        buf_len = len(text)
        buffer = ctypes.create_unicode_buffer(buf_len)
        buffer.value = text
        control.SendMessage(win32defines.WM_SETTEXT, buf_len, ctypes.byref(buffer))

    def get_control_text(self, control):
        buf_len = 1000
        buffer = ctypes.create_unicode_buffer(buf_len)
        num_chars = control.SendMessage(win32defines.WM_GETTEXT, buf_len, ctypes.byref(buffer))
        result = buffer.value
        return result

    def ask_question(self, question):
        self.set_control_text(self.question_box, question)
        self.sharpTona.Ask.Click()
        result = self.get_control_text(self.answer_box)
        logging.info(result)
        return result

    def verify_response_to_question(self, question, answer):
        result = self.ask_question(question)
        self.assertTextEqual(result, answer)

    ### Requirements tests ###

    @requirements(['#0001'])
    def test_window_title(self):
        window = self.app['SharpTona']
        self.assertIsNotNone(window)

    @requirements(['#0002'])
    def test_question_label(self):
        self.inspect_label('Question', 'Question:\w*')

    @requirements(['#0002'])
    def test_answer_label(self):
        self.inspect_label('Answer', 'Answer:\w*')

    @requirements(['#0003', '#0004'])
    def test_default_question(self):
        self.verify_response_to_question('What is the answer to everything?', '42')
        self.assertControlEnabled(self.answer_box)


    @requirements(['#0005', '#0006'])
    def test_default_application_state(self):
        sharpTona = self.app.sharpTona;
        self.assertControlDisabled(self.teach_button)
        self.assertControlDisabled(self.correct_button)
        self.assertControlVisible(self.answer_box)

    @requirements(['#0007'])
    def test_empty_question(self):
        self.verify_response_to_question('', 'Was that a question?')

    @requirements(['#0008', '#0009'])
    def test_answer_correction_flow(self):
        question = 'What is the answer to everything?'
        response = self.ask_question(question)
        expected_value = '43'
        self.set_control_text(self.answer_box, expected_value)
        self.assertControlEnabled(self.correct_button)
        self.correct_button.Click()
        self.assertControlDisabled(self.answer_box)
        self.assertControlDisabled(self.teach_button)
        self.assertControlDisabled(self.correct_button)
        self.verify_response_to_question(question, expected_value)
        self.set_control_text(self.answer_box, '42')
        self.correct_button.Click()

    @requirements(['#0011'])
    def test_teach_flow(self):
        question = 'Is this a question?'
        response = self.ask_question(question)
        expected_value = 'yes'
        self.set_control_text(self.answer_box, expected_value)
        self.assertControlEnabled(self.teach_button)
        self.teach_button.Click()
        self.assertControlDisabled(self.answer_box)
        self.assertControlDisabled(self.teach_button)
        self.assertControlDisabled(self.correct_button)
        self.verify_response_to_question(question, expected_value)

    @requirements(['#0010'])
    def test_unknown_question_response(self):
        self.verify_response_to_question('What is answer to this?', "I don't know please teach me.")
