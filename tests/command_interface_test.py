__author__ = 'drock'

from CommandInterface import *
from unittest import TestCase

class TestCommandInterface(TestCase, CommandHandler):
    def setUp(self):
        self.interpreter = CommandInterpreter(self)

    def test_quit_message(self):
        self.quit_hit = False
        self.interpreter.invokeCommand('X')
        self.assertEqual(self.quit_hit, True);

    def test_display_commands(self):
        self.display_commands_hit = False
        self.interpreter.invokeCommand('?')
        self.assertEqual(self.display_commands_hit, True)

    def quit(self):
        self.quit_hit = True;

    def displayCommands(self):
        self.display_commands_hit = True