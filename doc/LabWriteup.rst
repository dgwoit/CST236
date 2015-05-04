CST 236 Lab 4 Writeup
---------------------


Stage 1 CC
pyTona\answer_funcs.py
    F 4:0 feet_to_miles - A
    F 7:0 hal_20 - A
pyTona\main.py
    M 31:4 Interface.ask - C
    C 11:0 Interface - A
    M 61:4 Interface.teach - A
    M 69:4 Interface.correct - A
    M 12:4 Interface.__init__ - A
    M 75:4 Interface.__add_answer - A
pyTona\question_answer.py
    C 2:0 QA - A
    M 3:4 QA.__init__ - A

Stage 1 MI
pyTona\answer_funcs.py - A
pyTona\main.py - A
pyTona\question_answer.py - A
pyTona\__init__.py - A

Stage 2 CC
pyTona\answer_funcs.py
    F 68:0 get_fibonacci_seq - A
    F 16:0 get_git_branch - A
    F 27:0 get_git_url - A
    F 38:0 get_other_users - A
    M 63:4 FibSeqFinder.run - A
    F 10:0 feet_to_miles - A
    F 13:0 hal_20 - A
    C 54:0 FibSeqFinder - A
    M 55:4 FibSeqFinder.__init__ - A
    M 60:4 FibSeqFinder.stop - A
pyTona\main.py
    M 34:4 Interface.ask - C
    C 11:0 Interface - A
    M 63:4 Interface.teach - A
    M 71:4 Interface.correct - A
    M 12:4 Interface.__init__ - A
    M 77:4 Interface.__add_answer - A
pyTona\question_answer.py
    C 2:0 QA - A
    M 3:4 QA.__init__ - A

Stage 2 MI
pyTona\answer_funcs.py - A
pyTona\main.py - A
pyTona\question_answer.py - A
pyTona\__init__.py - A

Stage 3 CC

pyTona\answer_funcs.py
    F 68:0 get_fibonacci_seq - A
    F 16:0 get_git_branch - A
    F 27:0 get_git_url - A
    F 38:0 get_other_users - A
    M 63:4 FibSeqFinder.run - A
    F 10:0 feet_to_miles - A
    F 13:0 hal_20 - A
    C 54:0 FibSeqFinder - A
    M 55:4 FibSeqFinder.__init__ - A
    M 60:4 FibSeqFinder.stop - A
pyTona\main.py
    M 34:4 Interface.ask - C
    C 11:0 Interface - A
    M 63:4 Interface.teach - A
    M 71:4 Interface.correct - A
    M 12:4 Interface.__init__ - A
    M 77:4 Interface.__add_answer - A
pyTona\question_answer.py
    C 2:0 QA - A
    M 3:4 QA.__init__ - A

Stage 3 MI

pyTona\answer_funcs.py - A
pyTona\main.py - A
pyTona\question_answer.py - A
pyTona\__init__.py - A

pyTona\answer_funcs.py - A
pyTona\main.py - A
pyTona\question_answer.py - A
pyTona\__init__.py - A

1. What observations did you make while performing the analysis on the system?

Found several errors, one deleted requirement, need for additional requirements to achieve 100% code coverage.  Also
found Mock important for achieving 100% coverage for requirements.

What are the advantages/disadvantages of performing this analysis

This has proven to be very time consuming.  The details of getting Mock to work proved to be baffling because it would
fail with no indication as to why.

What are the advantages of data mutation? Did you use any of these tools?

Data mutation helps identify tests that never fail or do not have a dependency on the code, in which case those tests
fail to add value.

What did you use Mock for in this lab?

I used Mock to override various library methods so the unit tests could control the outcome of calls made by the
functions under test -- this way we have deterministic outcomes.

How long did this lab take to complete?

It seems like over 12 hours.  Itdentifying the information that successfully allowed Mocking the socket functions took
forever, just lots and lots of failure.  Mock seems very functionally expansive, and probably could have used more
concrete examples of usage.  Also it just seems like I'm fighting the tools and the code is running unexplainably slow.