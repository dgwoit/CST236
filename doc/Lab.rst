CST 236 Lab 3 Writeup
---------------------


1. What are five examples of other testing(nose2) plugins that might be useful?

* coverage - reports code coverage of tests
* doctests - executes test/example code in docs
* mp  - multiple processes, executes tests in
* profiling - perform test executing profiling
* testids - provides automatic generation of test ids

2. Do you plan to create any of these plugins for your term project?

Not entirely sure I understand the phrasing of the question.  If you mean "do I plan to use" any of these plugins for my
 term project I don't know at this time, but the coverage one will get use.  Do I plan to create any plugins for the
 term project? I don't yet see a need to do so.

3. What is the hardest part of this lab?
It seems like it took a while to assemble all of the tests together.  It really drove me crazy writing the testing plugin
because I missed the "always-on" setting for quite some time, which wasted loads of time.

4. Did the code fully and completely implement the requirements? Explain
No, the code did not fully implement the requirements.
* The ASCII code for the question mark was incorrectly stated as '0x3E', so this needs to be rectified.
* The distance conversion does not append miles to the result.
* The time calculation 1) does not calcuate the time 2) appends "seconds" to the result (not stated the requirements).
* The name of the inventor of Python is not reported to spec
* The format of the value to enter in for the time calculations is not specified anywhere

5. Was the requirements complete? Explain
The reporting of the time difference did not include to the time unit in the reported result, so this appears to be
inconsistent.  The program also lists the possible inputs, however this is not listed as a requirement, so this
discrepancy needs to be rectified as this could be an unrecorded requirement.

For each bug you found in the source code enter a "Bug Request" in your write up following this template. You should consider bugs to be not following the requirements, inaccurate requirements, or code that has no reason for existing (not covered by the requirements):
ISSUE Number:

**ISSUE Number:**

1

**BREIF:**

Character 0x3e (>) is being used as a question mark instead of 0x3f (?)

**Steps to reproduce:**:

Enter a question that ends in '>' instead of '?'

**Comments:**

This is a code defect and something that needs to be addressed in the requirements

**Time Spent:**

**ISSUE Number:**

2

**BREIF:**

42 seconds always reported in time calculation

**Steps to reproduce:**:

For "How many seconds since <date time>" provide a value that would not result in 42

**Comments:**

Suspect hard-coded response

**Time Spent:**

**ISSUE Number:**

3

**BREIF:**

"How many seconds since <date time>" report answer with "seconds" in response, however this is not specified anywhere.
"seconds" either needs to be removed OR the corresponding requirement needs to be updated.

**Steps to reproduce:**:
Use the "How many seconds since <date time>" function

**Comments:**

**Time Spent:**

**ISSUE Number:**

4

**BREIF:**

The "What is <float> feet in miles" function does not contain "miles" in the result.

**Steps to reproduce:**:

Use the "What is <float> feet in miles", view the result

**Comments:**

Requirement specify "miles" follows the number

**Time Spent:**

**ISSUE Number:**

5

**BREIF:**

Python inventor name incorrectly reported

**Steps to reproduce:**:

Use the "Who invented Python" function and observe the result.

**Comments:**

"Guido Rossum(Benevolent Dictator For Life)" is reported instead of "Guido Rossum(BFDL)"

**Time Spent:**


Why are requirements tracing so important?

Requirements tracing is important because

* it helps to verify each requirement has a test
* it helps to verify each test is traceable to a requirement
* it helps to keep automated tests maintainable and requirements ar subject to change

How long did it take to complete this lab?

It seems like I spent over eight hours on it, not really sure why it took that long, but it did.