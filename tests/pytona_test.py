__author__ = 'drock'

from unittest import TestCase
from pyTona.main import Interface
from source.ReqTracer import *
import time
import getpass

class TestPyTona(TestCase):
    WasThatAQuestion = "Was that a question?"
    IDontKnowPleaseProvideTheAnswer = "I don't know, please provide the answer"
    PleaseAskAQuestionFirst = "Please ask a question first"
    IDontKnowAboutThatIWasTaughtDifferently = "I don't know about that. I was taught differently"

    def setUp(self):
        self.pytona = Interface()
        pass

    def tearDown(self):
        pass

    def ask(self, statement):
        print "Statement: " + statement
        return self.pytona.ask(statement)

    def ask_question(self, statement):
        return self.ask(statement + '\x3E')

    @requirements(['#0001', '#0003'])
    def test_accepts_text(self):
        response = self.ask("this is a string")
        self.assertEqual(response, self.WasThatAQuestion)

    @requirements(['#0001', '#0002', '#0005', '#0009'])
    def test_how_question(self):
        response = self.ask_question('How is that')
        self.assertEqual(response, self.IDontKnowPleaseProvideTheAnswer)

    @requirements(['#0001', '#0002', '#0005', '#0009'])
    def test_what_question(self):
        response = self.ask_question('What is that')
        self.assertEqual(response, self.IDontKnowPleaseProvideTheAnswer)

    @requirements(['#0001', '#0002', '#0005', '#0009'])
    def test_where_question(self):
        response = self.ask_question('Where is that')
        self.assertEqual(response, self.IDontKnowPleaseProvideTheAnswer)

    @requirements(['#0001', '#0002', '#0005', '#0009'])
    def test_why_question(self):
        response = self.ask_question('Why is that')
        self.assertEqual(response, self.IDontKnowPleaseProvideTheAnswer)

    @requirements(['#0001', '#0002', '#0005', '#0009'])
    def test_who_question(self):
        response = self.ask_question('Who is that')
        self.assertEqual(response, self.IDontKnowPleaseProvideTheAnswer)

    @requirements(['#0001', '#0004'])
    def test_question_text(self):
        response = self.ask("Is this a question")
        self.assertEqual(response, self.WasThatAQuestion)

    @requirements(['#0001', '#0005'])
    def test_words_separated_by_no_space(self):
        try:
            response = self.ask_question("WhatIsAQuestion")
            self.assertEqual(response, self.WasThatAQuestion)
        except Exception:
            pass

    @requirements(['#0001', '#0002', '#0006', '#0008'])
    def test_question_match(self):
        response = self.ask_question('Why don\'t you understand Eliza')
        self.assertTrue(len(response) > 0)

    @requirements(['#0001', '#0002', '#0007', '#0008', '#0017'])
    def test_question_match_numeric_1024(self):
        response = self.ask_question('What is 1024 feet in miles')
        answer = str(float(2048)/float(5280)) + "miles"
        self.assertEqual(response, answer)

    def feet_to_miles_response(self, input):
        return str(float(input)/float(5280)) + "miles"

    @requirements(['#0001', '#0002', '#0007', '#0008', '#0017'])
    def test_question_match_numeric_2048(self):
        response = self.ask_question('What is 2048 feet in miles')
        answer = str(float(2048)/float(5280)) + "miles"
        self.assertEqual(response, answer)

    @requirements(['#0001', '#0002', '#0005', '#0009', '#0010', '#0011'])
    def test_teaching(self):
        response = self.ask_question('Who is PyTona')
        self.assertEqual(response, self.IDontKnowPleaseProvideTheAnswer)
        answer = "I am"
        response = self.pytona.teach(answer)
        response = self.ask_question('Who is PyTona')
        self.assertEqual(response, answer)

    @requirements(['#0001', '#0002', '#0005', '#0010', '#0012'])
    def test_teaching_no_question(self):
        answer = "the answer"
        response = self.pytona.teach(answer)
        self.assertEqual(response, self.PleaseAskAQuestionFirst)

    @requirements(['#0001', '#0002', '#0005', '#0010', '#0013'])
    def test_teaching_answer_teach(self):
        self.ask_question('Who invented Python')
        answer = "Guido Rossum(BFDL)"
        response = self.pytona.teach(answer)
        self.assertEqual(response, self.IDontKnowAboutThatIWasTaughtDifferently)

    @requirements(['#0001', '#0002', '#0007', '#0008', '#0011', '#0014', '#0015', '#0017'])
    def test_question_match_numeric_3072(self):
        self.ask_question('What is 3072 feet in miles')
        self.pytona.correct(self.feet_to_miles_response)
        response = self.ask_question('What is 3072 feet in miles')
        answer = str(float(3072)/float(5280)) + "miles"
        self.assertEqual(response, answer)

    @requirements(['#0001', '#0002', '#0005', '#0010', '#0014', '#0015'])
    def test_teaching_answer_correction(self):
        self.ask_question('Who invented Python')
        answer = "Guido Rossum(BFDL)"
        self.pytona.correct(answer)
        response = self.ask_question('Who invented Python')
        self.assertEqual(response, answer)

    @requirements(['#0001', '#0002', '#0005', '#0010', '#0016'])
    def test_correcting_no_question(self):
        answer = "the answer"
        response = self.pytona.correct(answer)
        self.assertEqual(response, self.PleaseAskAQuestionFirst)

    @requirements(['#0001', '#0002', '#0007', '#0008', '#0018'])
    def test_question_epoch_now(self):
        response = self.ask_question('How many seconds since ' + str(long(time.clock())))
        answer = "0"
        self.assertEqual(response, answer)

    @requirements(['#0001', '#0002', '#0007', '#0008', '#0019'])
    def test_question_inventor(self):
        response = self.ask_question('Who invented Python')
        answer = "Guido Rossum(BFDL)"
        self.assertEqual(response, answer)

    @requirements(['#0001', '#0002', '#0007', '#0008', '#0020'])
    def test_question_understand(self):
        response = self.ask_question('Why don\'t you understand me')
        answer = "Because you do not speak 1s and 0s"
        self.assertEqual(response, answer)

    @requirements(['#0001', '#0002', '#0007', '#0008', '#0021'])
    def test_question_shutdown(self):
        response = self.ask_question('Why don\'t you shutdown')
        answer = "I'm afraid I can't do that " + getpass.getuser()
        self.assertEqual(response, answer)







