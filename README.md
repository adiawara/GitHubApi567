
Mock the GitHub API
In last week's assignment HW 04a you may have encountered problems when testing your code in Travis-CI given that your tests were highly dependent on the GitHub APIs.   Those APIs would start to return errors if you exceeded a threshold on use, or those APIs would return different results if you make a change to your repos.    Remember that one of the key concepts behind unit-tests was that if you don't change your program then the unit-tests should behave consistently.  Unfortunately that is not the case so far. 

In this assignment you will use a mocking package to "mock" your program's external dependence on GitHub, so that you can guarantee that your unit tests will run consistently ever time you run them, no matter how many times you run them, and no matter what changes you make to your repos.

Instructions
Start with the GitHub API program that you completed in HW 4a and mock out all of the service calls in that program using the python mock module.   

For this assignment you won't need to create any new repository; instead you will make all of your changes in the same repository that you used for HW 4a.   In order to separate what you do in this assignment from what you did in HW 4a, we will make use of git branching.  For HW 04a all of your code should be on the "master" branch of your repository.  For this assignment you will make all of your changes on a different branch named "HW05a_Mocking".   You will need to create this new branch.

You can either create the branch locally on your laptop and then push the branch and its associated changes up to GitHub, or you can create the branch in GitHub and pull that branch down to your local repository.    Once you have your new branch, then all changes for mocking your API calls should go on that branch.

Note that when you are making any changes to the programs on the "HW05a_Mocking" branch, that you should not make any changes to the program that is calling the GitHub APIs using the requests module..  Rather, all of your changes that you make in the "HW05a_Mocking" branch should be in two files:  (1) the file containing the unit tests, and (2) the README file.  The README file for the branch should be updated so that the badge shows the status of your unit tests for the code on the "HW05a_Mocking" branch.  If you don't make any changes to it then the badge will show the status of your code on the "master" branch.

When you are done you should then be able to run your tests on Travis-ci and it should not make any calls to GitHub.  You will have eliminated all dependencies to the GitHub APIs.

With Python 3, the mock package is already part of the unittest module as unittest.mock 

Check out these links which might be useful to you:

https://blog.fugue.co/2016-02-11-python-mocking-101.html 


https://medium.com/python-pandemonium/python-mocking-you-are-a-tricksy-beast-6c4a1f8d19b2 


https://realpython.com/blog/python/testing-third-party-apis-with-mocks/ 

 

Deliverables:
Submit the GitHub URL of the repository containing your code (should be the same as what you submitted for HW 04a).  .   My expectation will be that

1. all of your changes for this assignment will be on the branch "HW05a_Mocking"

2. the README file will contain a badge that links to the build status of your code on the branch "HW05a_Mocking" running in Travis-CI.

3. the build status will be success

[![build status of master](https://travis-ci.org/adiawara /HW05a_Mocking.svg?branch=master)](https://travis-ci.org/adiawara/HW05a_Mocking)![image](https://user-images.githubusercontent.com/22464380/143682884-6f0082f3-eb77-4290-8a8e-b62777e87835.png)
