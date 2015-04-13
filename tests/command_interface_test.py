__author__ = 'drock'

from CommandInterface import *
from unittest import TestCase

class TestCommandInterface(TestCase, CommandHandler):
    def test_quit_message(self):
        interpreter = CommandInterpreter(self)
        self.quit_hit = False
        interpreter.invokeCommand('X')
        self.assertEqual(self.quit_hit, True);

    def quit(self):
        self.quit_hit = True;