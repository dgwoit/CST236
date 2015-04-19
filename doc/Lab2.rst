CST 236 Lab 2 Writeup
---------------------

1. Explain the major differences between TDD and BDD

In BDD the user story is converted to a normal language spec before TDD begins.  BDD also makes implementation easier to understand

2. What is a mixin, what challenges can occur when testing them? What order are they initialized in

Mixins are where a class has multiple inheritance.
I suppose the challenge would be in testing all of the behaviors provided by the base classes in the child class.
Per the Lab2.rst document Mixins are initialized in order.

3. In python what does "super" do?

"Return a proxy object that delegates method calls to a parent or sibling class of type."  Super is used to access methods/attributes of a base class.

4. Was there any job stories that did not meet the criteria we discussed in class? How did you handle this case?

As far as I can tell the Job stories appear to adhere to the Job Story format.

5. Which model did you find most challenging? Why?

Sadly I haven't made it to the BDD section of the lab yet as it seems I have lost a lot of time dealing with various issues.  This approach of using multiple new tools at once seems problematic.

6. Which model did you find easiest to update/maintain?

I don't know yet, perhaps I'll get to find out when circumstances are more in my favor.

7. How did you test that logging occurred only when desired?

I based my testing on this example (http://stackoverflow.com/questions/9534245/python-logging-to-stringio-handler) where
stream I/O is being used to capture the log data.  Setting/getting the logger by data and setting the log level are already part of the logger.