"""
:mod:`source.CommandInterface` -- Command Interface Subsystem
============================================

This module contains classes involved with interpreting and executing user commands
"""

import logging

"""
:class:'Command Handler'
:purpose: Receives interpreted command requests from the command interpreter
"""
class CommandHandler(object):
    """
    :function:'quit'
    :purpose: receives the quit event. Overload to handle "quit" in your program
    :arguments: none
    :returns: none
    """
    def quit(self):
        return

    def displayCommands(self):
        return

"""
:class: 'Command Interpreter'
:purpose: Parses text input and issues commands based on input
"""
class CommandInterpreter:
    """
    :function: __init__
    :purpose: class initiator
    :arguments:
        :param handler: The CommandHandler instance to send commands to
    :returns: none
    """
    def __init__(self, handler):
        self.handler = handler

    """
    :function: invokeCommand
    :purpose: invokes commands based on text inpu
    :arguments:
        :param str_cmd: the string command to interpret
    """
    def invokeCommand(self, str_cmd):
        if(str_cmd == 'X'):
            self.handler.quit()
        elif(str_cmd == '?'):
            self.handler.displayCommands()
        else:
            logging.getLogger().warn('Bad command ' + str_cmd)
