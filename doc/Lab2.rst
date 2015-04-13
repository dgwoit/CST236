CST 236 Lab 1 Writeup
---------------------


1. What was the hardest part of this lab?
Installing and trying to understand the instructions for git.  Had I known Tortoisegit existed before-hand I would have
installed that first since I'm not writing SVN scripts.  Also the lab instructions for git were a bit sparse in areas.

2. During the course of this lab, why did we exclude .pyc files?
.pyc files are not text files and are generated from .py files, as such they are not a good candidate for storing in a
repository.

3. Name three files which would likely need to have a gitignore added?
Assuming by files we are talking about files and not files & folders I would say .pyc files, html files, and .exe files
(listed automatically in the .gitignore, but there are no .exe files for this lab)

4. What is a pyunit TestCase?
A pyunit TestCase is a class derived from TestCase containing zero to many function definitions for individually
executing a test case each for a target piece of code/functionality.

5. What is the difference between a git cherry pick and a rebase?
git cherry-pick allows the user to determine which changes are merged to base.  Rebase merges all changes to base.

6. How could you use git to print out just the author name of a given file for the current version of the repo?

.. code::

    git log --max-count=1 --author <path>

7. During this lab did you explore Tortoise Git or GIT Extensions? If not take a look at them, they probably would be useful for the remainder of the class
No I did not explore Tortoise Git as I was unaware of its existence.

8. Did you find the second issue in get_triangle_type? Did you choose to test the code as is or fix the code in get_triangle_type
I saw the error but left it alone as I did not see any instructions directing me to resolve the issue, nor were there any prior suggestions there may be a bug.