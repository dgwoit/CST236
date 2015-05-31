CST 236 Lab 8 Writeup
---------------------

Analysis Questions
******************

1. How was this test useful?

Test performs a basic level of smoke testing to verify the product is capable of being tested, either manually or automatically.  If the system under test is unable to load, classes are uninstantiable, or functions cannot be called then errors will occur during testing if the system is capable of loading.

2. How did you report errors found by this test? How difficult would it be for a developer to debug these errors

Errors, and warnings are reported to the console.  Counts of passes, warnings and failures are reported in a summary at the end of the report.  When failures occur the statements state what kind of failure occurred, and what item was under test.

3. What other things would be useful to have in a sanity test?

We could check for memory leaks after unloading everything.  We could also randomize the order of the sanity tests in case there is a bug dependent on the order of execution.  We could check the methods in a class. We could verify all required files are present.

4. How would you sanity test a UI? A database interface? a webpage? a C# program?

* For UIs we could verify various UI elements are loadable/present such as dialogs, windows, menus.  Verify resource files are present.
* For database interface we could verify CRUD methods are callable.  We could enumerate the tables, fields, keys, etc in the database.  We can verify the database is accessible as databases are accessed via various communication methods (e.g. TCP/IP).
* For web pages we could verify pages are loadable.
* For C# programs we could verify all assemblies are present, verify classes can be instantiated, functions called, class methods called.  We could smoke test the system.