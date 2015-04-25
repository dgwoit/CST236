Source Example
========================

CommandInterface provides basic handling of textual user input


class CommandHandlerImpl(CommandHandler)
    def quit(self):
        print 'time to quit!'

handler = CommandHandler()
interpreter = CommandInterpeter(handler)
interpreter('X')

Module Reference
^^^^^^^^^^^^^^^^

.. automodule:: source.CommandInterface
    :members: