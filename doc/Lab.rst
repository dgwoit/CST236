CST 236 Lab 6 Writeup
---------------------

Manual Tests
************

**Startup Application State**

*Setup*

#. Sharp sharpTona.exe

*Procedure*

#. Verify window title is "SharpTona"
#. Verify the "Teach" button is disabled
#. Verify the "Correct" button is disabled

**Edit Box Labels**

*Setup*

#. Start sharpTona.exe

*Procedure*

#. Verify there is a "Question:" label
#. Verify there is an "Answer:" label

**Question Answer Response**

*Setup*

#. Start sharpTona.exe

*Procedure*

#. Enter the question "What is the answer to everything?" in the question box
#. Verify the result in the answer box is "42"
#. Verify the answer box is now enabled

**Empty Question**

*Setup*

#. start sharpTona.exe

*Procedure*

#. Press the "Ask" button
#. Verify the answer box contains "Was that a question?"

**Correcting an Answer**

*Setup*

#. Start sharpTona.exe
#. Either teach the system an answer to question or use a known question/answer pair

*Procedure*

#. Enter the question in the question box
#. Press the "Ask" button
#. Enter a different value in the answer box
#. Press the "Correct" button
#. Press the "Ask" button
#. Verify the answer in the answer box is the one the tester changed

**Unknown Question**

*Setup*

#. start sharpTona.exe

*Procedure*

#. Enter a question unknown to the system in the answer box
#. Press the "Ask" button
#. Verify the answer box contains "I don't know please teach me."
#. Verify the "Teach" button is enabled
#. Press the "Teach" button
#. Verify the "Teach" button is disabled
#. Verify the "Correct" button is disabled
#. Verify the answer box is disabled
#. Verify the stored answer can be retrieved when the question is asked again

Analysis Questions
******************

1. What are the advantages and disadvantages of manual testing?

The chief disadvantage of manual testing is it's manual nature.  Having people people perform repetitive testing can
impair morale (I lost a tester this way).

Manual testing provides an opportunity to perform exploratory testing where a tester can utilize their own intelligence
to inquire about the proper/desired operation of a product.  Manual testing also allows the tester to observe product
behavior and presentation that would not be caught by established automated testing

2. What are the advantages and disadvantages of automated testing?

Automated testing is excellent for determining whether the product is operating in repeatable fashion.  Automated testing
can operate continuously, unlike people, and is useful for continuous integration testing.  Automated tests are limited by
the boundaries of their coding, and for example, can be poor judges of product usability and appeal.

3. What new bugs did you encounter with the new code?

One of the control labels contained extra whitespace.  Aside from that there are other behaviors that may be inconsistent
from prior labs and could be grounds for interacting with those responsible for authoring the user stories.

4. How many UI tests did you generate? How did you determine you had written enough?

There are nine tests total, however those tests perform multiple steps for setup and test for a variety of conditions
along the way, so effectively we may have double that.  Test cases stopped being written when we had covered the requirements as we
don't have the ability to view code coverage, or to review the code to look for other concepts in testing.

5. How long did this lab take to accomplish?

I think maybe 8 hours.  I think about three of those hours were due to behaviors relating to GetWindowText.  Also I
don't think skipping lunch helped any.