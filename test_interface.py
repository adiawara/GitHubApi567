
# -*- coding: utf-8 -*-
"""
Each Status-Code, including a description of which method(s)
it can follow and any metainformation required in the response, is described in the below url link.
w3.org/Protocols/rfc2616/rfc2616-sec10.html#:~:text=2%20201%20Created,by%20a%20Location%20header%20field.
"""

import unittest
import interface
from interface import*
from interface import numberReposandCommits

class TestGithubApi(unittest.TestCase):
    # Type of function selected by a Developer in a Tester mind

    def test_requestStatus(self):
        try:
            userDatatest = numberReposandCommits(user)
            self.assertEqual(userDatatest["requestStatus"],200)
        except:
            print("Test Failed")
        else:
            print("Test succeed")
    
    def test_On_numberOfRepositories(self): 
        try:
             userDatatest = numberReposandCommits(user)
             self.assertEqual(userDatatest["numberOfRepos"],9)
        except:
            print("Test Failed")
        else:
            print("Test succeed")
    
    def test_userID(self):
        try:
             userDatatest = numberReposandCommits(user)
             self.assertEqual(userDatatest["id"],"richkempinski")
        except:
            print("Test Failed")
        else:
            print("Test succeed")
    
if __name__ == '__main__':
    print('       unit tests  ....  ')
    unittest.main(exit=False)


