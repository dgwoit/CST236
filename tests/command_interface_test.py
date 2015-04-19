__author__ = 'drock'

from CommandInterface import *
from unittest import TestCase

class TestCommandInterface(TestCase, CommandHandler):
    """
    TestCommandInterface
    """
    def setUp(self):
        self.interpreter = CommandInterpreter(self)

    def test_quit_message(self):
        self.quit_hit = False
        self.interpreter.invoke_command('X')
        self.assertEqual(self.quit_hit, True);

    def test_display_commands(self):
        self.display_commands_hit = False
        self.interpreter.invoke_command('?')
        self.assertEqual(self.display_commands_hit, True)

    def test_destroy_all_orcs(self):
        self.destroy_all_orcs_hit = False
        self.interpreter.invoke_command("ENTer the Trees")
        self.assertTrue(self.destroy_all_orcs_hit)

    def quit(self):
        self.quit_hit = True;

    def display_commands(self):
        self.display_commands_hit = True

    def destroy_all_orcs(self):
        self.destroy_all_orcs_hit = True