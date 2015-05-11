__author__ = 'drock'

from unittest import TestCase
from pyTona.main import Interface
from pyTona.answer_funcs import *
from source.ReqTracer import *
from source.PerformanceDecorator import performance
from mock import Mock
from mock import patch
from socket import socket
import time
import getpass
import subprocess
import socket
import math
import threading
import random
import logging

class TestPyTona(TestCase):
    WasThatAQuestion = "Was that a question?"
    IDontKnowPleaseProvideTheAnswer = "I don't know, please provide the answer"
    PleaseAskAQuestionFirst = "Please ask a question first"
    IDontKnowAboutThatIWasTaughtDifferently = "I don't know about that. I was taught differently"
    NotAString = "Not A String!"
    TooManyExtraParameters = "Too many extra parameters"

    def setUp(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.pytona = Interface()

    def tearDown(self):
        if None != seq_finder:
            seq_finder.stop()
            seq_finder.join()

        for t in threading.enumerate():
            if threading.current_thread() != t:
                t.stop()
        pass

    def ask(self, statement):
        self.logger.info("Statement: " + statement)
        return self.pytona.ask(statement)

    def ask_question(self, statement):
        return self.ask(statement + '\x3F')

    @requirements(['#0001', '#0003'])
    def test_accepts_text(self):
        response = self.ask("this is a string")
        self.assertEqual(response, self.WasThatAQuestion)

    @requirements([])
    def test_nontext_fails(self):
        try:
            response = self.pytona.ask(5)
        except Exception as e:
            self.assertEqual(e.message, self.NotAString)

    @requirements([])
    def test_too_many_extra_parameters(self):
        self.ask_question("How about an exception")
        def thrower():
            raise Exception("here it is")
        self.pytona.teach(thrower)
        try:
            response = self.ask_question("How about an exception")
        except Exception as e:
            self.assertEqual(e.message, self.TooManyExtraParameters)

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
        answer = self.feet_to_miles_response(1024)
        self.assertEqual(response, answer)

    def feet_to_miles_response(self, input):
        return str(float(input)/float(5280)) + " miles"

    @requirements(['#0001', '#0002', '#0007', '#0008', '#0017'])
    def test_question_match_numeric_2048(self):
        response = self.ask_question('What is 2048 feet in miles')
        answer = self.feet_to_miles_response(2048)
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
        answer = "Guido Rossum(BDFL)"
        response = self.pytona.teach(answer)
        self.assertEqual(response, self.IDontKnowAboutThatIWasTaughtDifferently)

    @requirements(['#0001', '#0002', '#0007', '#0008', '#0011', '#0014', '#0015', '#0017'])
    def test_question_match_numeric_3072(self):
        self.ask_question('What is 3072 feet in miles')
        self.pytona.correct(self.feet_to_miles_response)
        response = self.ask_question('What is 3072 feet in miles')
        answer = self.feet_to_miles_response(3072)
        self.assertEqual(response, answer)

    @requirements(['#0001', '#0002', '#0005', '#0010', '#0014', '#0015'])
    def test_teaching_answer_correction(self):
        self.ask_question('Who invented Python')
        answer = "Guido Rossum(BDFL)"
        self.pytona.correct(answer)
        response = self.ask_question('Who invented Python')
        self.assertEqual(response, answer)

    @requirements(['#0001', '#0002', '#0005', '#0010', '#0016'])
    def test_correcting_no_question(self):
        answer = "the answer"
        response = self.pytona.correct(answer)
        self.assertEqual(response, self.PleaseAskAQuestionFirst)

    @requirements(['#0001', '#0002', '#0007', '#0008', '#0019'])
    def test_question_inventor(self):
        response = self.ask_question('Who invented Python')
        answer = "Guido Rossum(BDFL)"
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

    def get_git_branch(self):
        try:
            process = subprocess.Popen(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], stdout=subprocess.PIPE)
            output = process.communicate()[0]
        except:
            return "Unknown"

        if not output:
            return "Unknown"
        return output.strip()

    @requirements(['#0001', '#0002', '#0007', '#0008', '#0022'])
    def test_question_branch(self):
        response = self.ask_question("Where am I")
        answer = self.get_git_branch()
        self.assertEqual(response, answer)

    @requirements(['#0001', '#0002', '#0007', '#0008', '#0022'])
    def test_git_branch_exception(self):
        with patch("subprocess.Popen") as mock:
            mock().communicate.side_effect = Exception("fail")
            response = self.ask_question("Where am I")
            self.assertEqual(response, "Unknown")

    @requirements(['#0001', '#0002', '#0007', '#0008', '#0022'])
    def test_git_branch_unknown(self):
        with patch("subprocess.Popen") as mock:
            mock().communicate.return_value = [None]
            response = self.ask_question("Where am I")
            self.assertEqual(response, "Unknown")

    @staticmethod
    def get_git_url():
        try:
            process = subprocess.Popen(['git', 'config', '--get', 'remote.origin.url'], stdout=subprocess.PIPE)
            output = process.communicate()[0]
        except:
            return "Unknown"

        if not output:
            return "Unknown"
        return output.strip()

    def equality_test(self, question, answer):
        response = self.ask_question(question)
        self.assertEqual(response, answer)

    @requirements(['#0001', '#0002', '#0007', '#0008', '#0023'])
    def test_question_repo(self):
        self.equality_test("Where are you", self.get_git_url())

    @requirements(['#0001', '#0002', '#0007', '#0008', '#0023'])
    def test_git_branch_unknown(self):
        with patch("subprocess.Popen") as mock:
            mock().communicate.side_effect = Exception("failure")
            response = self.ask_question("Where are you")
            self.assertEqual(response, "Unknown")

    @requirements(['#0001', '#0002', '#0007', '#0008', '#0023'])
    def test_git_branch_unknown(self):
        with patch("subprocess.Popen") as mock:
            mock().communicate.return_value = [None]
            response = self.ask_question("Where are you")
            self.assertEqual(response, "Unknown")

    @requirements(['#0001', '#0002', '#0007', '#0008', '#0024', '#0026'])
    def test_question_users(self):
        def connect(address):
            print "connect"
            return

        def send(data):
            pass

        def recv():
            return 'chico$harpo$groucho$gummo$zeppo'

        with patch("socket.socket") as mock:
            mock().connect.side_effect = connect
            mock().send.side_effect = send
            mock().recv.return_value = 'chico$harpo$groucho$gummo$zeppo'
            self.equality_test("Who else is here", ["chico", "harpo", "groucho", "gummo", "zeppo"])
            mock().send.assert_called_once_with('Who?')
            mock().connect.assert_called_once_with(('192.168.64.3',1337))

    @requirements(['#0001', '#0002', '#0007', '#0008', '#0025', '#0026'])
    def test_question_users_trap(self):
        with patch("socket.socket") as mock:
            mock().connect.side_effect = Exception("fail")
            self.equality_test("Who else is here","IT'S A TRAAAPPPP")

    def Fib(self, n):
        if n == 0: return 0
        elif n == 1: return 1
        else: return self.Fib(n-1)+self.Fib(n-2)

    @requirements(['#0001', '#0002', '#0007', '#0008', '#0028'])
    def test_question_fib_0(self):
        self.equality_test("What is the 0 digit of the Fibonacci sequence", self.Fib(0))

    @requirements(['#0001', '#0002', '#0007', '#0008', '#0028'])
    def test_question_fib_101(self):
         fib = FibSeqFinder()
         fib.start()
         while(len(fib.sequence) <= 101):
             time.sleep(1.0)
             continue
         self.assertEqual(fib.sequence[5], self.Fib(5))
         fib.stop()
         fib.join()

    """
    multinomial distribution

    mu=n*p, variance=n*p*(1-p)
    sigma = sqrt(variance)

    Test to see if the number of occurrences of an outcome is withing two standard deviations, otherwise outcomes
    are suspect
    """
    def multinomial_test(self, num_trials, occurrences, p):
        mu = num_trials * p
        sigma = math.sqrt(num_trials * p * (1.0 - p))
        self.assertTrue(occurrences <= mu+2*sigma)
        self.assertTrue(occurrences >= mu-2*sigma)

    @requirements(['#0001', '#0002', '#0007', '#0008', '#0029'])
    def test_question_fib_n(self):
        count = 0
        thinking_count = 0
        one_second_count = 0
        cool_your_jets_count = 0
        self.randstate = 0
        reset_seq_finder()
        def my_randint(self, min, max):
            val = self.randstate;
            randstate = int((self.randstate + 1) % 10)
            return val
        with patch("random.random") as mock:
            mock().randint.side_effect = my_randint
            for n in range(0, 1000):
                question = "What is the 1000 digit of the Fibonacci sequence\x3f"
                result = self.pytona.ask(question)

                if result is int or result is long:
                    continue

                #accumulate stats for different outcomes
                count += 1
                if result == "Thinking...":
                    thinking_count += 1
                elif result == "One second":
                    one_second_count += 1
                elif result == "cool your jets":
                    cool_your_jets_count += 1
                else:
                    logger.info(result)
                    pass
            self.logger.info("thinking count: " + str(thinking_count))
            self.logger.info("one second count: " + str(one_second_count))
            self.logger.info("cool your jets count: " + str(cool_your_jets_count))
            self.multinomial_test(count, thinking_count, 0.60)
            self.multinomial_test(count, one_second_count, 0.30)
            self.multinomial_test(count, cool_your_jets_count, 0.10)

    @requirements(['#0001', '#0002', '#0008', '#0010', '#0011', '#0015', '#0030'])
    def test_qa_pair_capacity(self):
        for n in range(1, 1000000):
            self.pytona.ask("Why x%(x)x\x3f"%{"x", n})
            self.pytona.teach(str(n))
        for n in range(1, 1000000):
            self.equality_test("Why x%"%{"x", n}, str(n))

    @requirements(['#0001', '#0002', '#0008', '#0010', '#0011', '#0015', '#0031'])
    @performance()
    def test_answer_store_time(self):
        question = "What is the answer"
        answer = "42"
        self.ask_question(question)
        samples = 100
        start_time = time.clock()
        for n in range(1, samples):
            self.pytona.teach(answer)
        stop_time = time.clock()
        response_time = (stop_time - start_time) / samples
        self.assertTrue(response_time < 5)

    @requirements(['#0001', '#0002', '#0008', '#0010', '#0011', '#0015', '#0032'])
    @performance()
    def test_answer_retrieve_time(self):
        question = "What is the answer\x3f"
        answer = "42"
        self.pytona.ask(question)
        self.pytona.teach(answer)
        samples = 100
        start_time = time.clock()
        for n in range(1, samples):
            response = self.pytona.ask(question)
            self.assertEqual(response, answer)
        stop_time = time.clock()
        response_time = (stop_time - start_time) / samples
        self.assertTrue(response_time <= 5)

    def ask_fib_question(self, n):
        return self.ask_question("What is the {0} digit of the Fibonacci sequence".format(n))

    @requirements(['#0033'])
    def test_fibonacci_termination(self):
        self.ask_fib_question(1001)
        finder = get_seq_finder()
        self.assertTrue(finder)
        while finder.is_alive():
            time.sleep(1)
        self.assertTrue(finder.num_indexes == 1000)

    @requirements(['#0034'])
    @performance()
    def test_fibonacci_performance(self):
        start_time = time.clock()
        finder = get_seq_finder()
        self.test_fibonacci_termination()
        end_time = time.clock()
        duration = end_time - start_time
        self.assertTrue(duration < 60)

    @requirements(['#0035'])
    def test_pi_calculation(self):
        response = self.ask_question("What is PI for 1000 samples")
        self.logger.info("pi estimate: " + str(response))
        self.assertTrue(response > 0.9*math.pi)
        self.assertTrue(response < 1.1*math.pi)

    @requirements(['#0036'])
    @performance()
    def test_pi_performance(self):
        start_time = time.clock()
        response = self.ask_question("What is PI for 1000 samples")
        logger.info(str(response))
        end_time = time.clock()
        duration = end_time - start_time
        self.assertTrue(duration < 60)

    @requirements(['#0037'])
    def test_e_calculation(self):
        question = "What is E to the 10 calculation"
        self.ask_question(question)
        response = self.ask_question(question)
        n = 0
        while response is not float and n < 60:
            time.sleep(1)
            response = self.ask_question(question)
            self.logger.info(type(response))
            self.logger.info(response)
            n += 1
        self.assertTrue(response > 0.9*math.e)
        self.assertTrue(response < 1.1*math.e)

    @requirements(['#0038'])
    @performance()
    def test_e_performance(self):
        start_time = time.clock()
        self.ask_question("What is E to the 10 calculation")
        end_time = time.clock()
        duration = end_time - start_time
        self.assertTrue(duration < 60)

    @requirements(['#0039'])
    def test_mandelbrot_calculation(self):
        question = "What is Mandelbrot area for 1000 samples"
        response = self.ask_question(question)
        self.logger.info(response)
        sampler = get_mandelbrot_sampler()
        sampler.join()
        response = self.ask_question(question)
        self.logger.info("response: " + str(response))
        known_value = 1.5065918849
        self.assertTrue(response > 0.7*known_value)
        self.assertTrue(response < 1.4*known_value)

    @requirements(['#0040'])
    @performance()
    def test_mandelbrot_performance(self):
        start_time = time.clock()
        self.test_mandelbrot_calculation()
        stop_time = time.clock()
        duration = stop_time - start_time
        self.assertTrue(duration < 60)

    @requirements(['#0041'])
    def test_lorem_ipsum(self):
        question = "How many words in Lorem Ipsum"
        answer = 10611
        self.equality_test(question, answer)

    @requirements(['#0042'])
    @performance()
    def test_lorem_ipsum_performance(self):
        start_time = time.clock()
        for n in range(0,1000):
            self.test_lorem_ipsum()
        stop_time = time.clock()
        duration = stop_time - start_time
        self.assertTrue(duration)
        assert(duration < 60)


