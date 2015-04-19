"""
:mod:`source.CommandInterface` -- Command Interface Subsystem
============================================

This module contains classes involved with interpreting and executing user commands
"""

import logging

class CommandHandler(object):
    """
    Command Handler
    """
    def quit(self):
        """
        Quit program
        :return: none
        """
        pass

    def display_commands(self):
        """
        Display all commands
        :return: none
        """
        pass

    def destroy_all_orcs(self):
        """
        Destroys all orcs in the game
        :return: none
        """
        pass


class CommandInterpreter:
    """
    Command Interpreter
    """

    def __init__(self, handler):
        """
        class initiator
        :param handler: derived instance of handler to receive the commands
        :type handler: CommandHandler
        """
        self.handler = handler


    def invoke_command(self, str_cmd):
        """
        Invokes Command
        :param str_cmd: the string command to execute
        :type str_cmd: string
        :return: None
        """

        if(str_cmd == 'X'):
            self.handler.quit()
        elif(str_cmd == '?'):
            self.handler.display_commands()
        elif(str_cmd == "ENTer the Trees"):
            self.handler.destroy_all_orcs()
        else:
            logging.getLogger().warn('Bad command ' + str_cmd)
