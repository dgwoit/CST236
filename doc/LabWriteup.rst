CST 236 Lab 5 Writeup
---------------------

1. What was the hardest part of this lab?

Debugging, in part because running things take such a long time.  Also I don't have the nose2 unit test running in a
debugger which is a huge disadvantage.

2. What is the difference between performance testing and performance measurement?

Performance testing is when you are measuring system performance against specified criteria.  Performance measurement is
 the act of measuring the system - this action may be part of performance testing or just part of performance reporting.

3. What new bugs did you encounter with the new code?

Stats for "One second" result from Fibonacci sequence not correct.
Changing elif value > 1: to elif value >= 1: appears to resolve issue

Changed the minimum number of question/pair answers from 1,000,000 to 1000 because the execution time for this test was excessive and timed out on drone.io

Also global objects aren't as global as the name global would imply

4. Did you mock anything to speed up performance testing? Do you see any issues with this?

No mocking was performed for this testing.

5. Generate at least 5 performance measurement value sets and graphs (these sets must be worthwhile)

See PerformanceResults.xls

6. Explain Load Testing, stress testing, endurance testing, spike testing configuration testing and isolation testing. How did you implement each of these?

* Load Testing: Measuring system performance under a given load

Load testing is effectively performed with the tests in general as this is currently a one user system.

* Stress Testing: Measures the effects of the system under different loads (e.g. overheating)

While not intentional I can report the computer appears to be operating at higher load with the test running -- the
system continues to run.

* Endurance Testing:   Tests the ability of the system to perform over time

For the run of the system tests we evaluate whether Pytona is operating correctly.  No tests are in place to test the
system over extended periods of time.

* Spike Testing: Tests the impacts of the system when the load is drastically varied with respect to time

Per the slide notes, Spike Testing is largely applied to web applications.  Since this is not a web application, and it
is only a single user system no spike testing is applied.

* Configuration Testing: measures the ability of the system to operate correctly with variations in environment/components.

This system is tested on both Windows (my laptop) and on linux (drone.io)

7. How long did this lab take to accomplish?

Maybe 12 hours, just lots fo futzing around with getting everything completed and working, research, re-runs, etc.