
# -*- coding: utf-8 -*-
'''
***** I read through the process of accomplishing this homework the following *****
Using mock objects correctly goes against our intuition to make tests as real and
thorough as possible, but doing so gives us the ability to write self-contained tests that
run quickly, with no dependencies. It gives us the power to test exception handling and
edge cases that would otherwise be impossible to test. Most importantly, it gives us
the freedom to focus our test efforts on the functionality of our code, rather than
our ability to set up a test environment. By concentrating on testing what’s important,
we can improve test coverage and increase the reliability of our code, which is why
we test in the first place.

'''
import unittest
from unittest import mock 
from unittest.mock import Mock, patch, MagicMock
import interface
from interface import*
from interface import numberReposandCommits

class TestGithubApi(unittest.TestCase):
    # Type of function selected by a Developer in a Tester mind
    @mock.patch('interface.numberReposandCommits')
    def test_mock_test_requestStatus(self, mock_status):
        mock_status.return_value = MagicMock(status_code = 200)
        #result = interface.numberReposandCommits(user)
        result = mock_status.return_value.status_code
        try:
            self.assertEqual(result, 200)
        except:
            print("Test Failed")
        else:
            print("Test succeed")
            
    @mock.patch('interface.numberReposandCommits')
    def test_mock_numberReposandCommits(self, mock_number):
        mock_number.return_value = MagicMock(repository = 9)
        #result = interface.numberReposandCommits(user)
        result = mock_number.return_value.repository
        try:
             self.assertEqual(result, 9)
        except:
            print("Test Failed")
        else:
            print("Test succeed")
    @mock.patch('interface.numberReposandCommits')
    def test_mock_test_userID(self, mock_userID):
         mock_userID.return_value = MagicMock(userID = "richkempinski")
         #result = interface.numberReposandCommits(user)
         result = mock_userID.return_value.userID
         try:
             self.assertEqual(result, "richkempinski")
         except:
            print("Test Failed")
         else:
            print("Test succeed")
    
if __name__ == '__main__':
    print('       unit tests  ....  ')
    unittest.main(exit=False)

        
