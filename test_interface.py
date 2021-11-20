
# -*- coding: utf-8 -*-
"""
Each Status-Code, including a description of which method(s)
it can follow and any metainformation required in the response, is described in the below url link.
w3.org/Protocols/rfc2616/rfc2616-sec10.html#:~:text=2%20201%20Created,by%20a%20Location%20header%20field.
"""

import unittest

from interface import numberReposandCommits

class TestGithubApi(unittest.TestCase):
    # Type of function selected by a Developer in a Tester mind

    def test_requestStatus(self): 
        self.assertEqual(numberReposandCommits("checkOnStatusCode 100 continue")["requestStatus"],100)
    def test_requestStatus(self): 
        self.assertEqual(numberReposandCommits("checkOnStatusCode 101 Switching Protocols")["requestStatus"],101)
    def test_requestStatus(self): 
        self.assertEqual(numberReposandCommits("checkOnStatusCode 200 OK")["requestStatus"],200)
    def test_requestStatus(self): 
        self.assertEqual(numberReposandCommits("checkOnStatusCode 202 Accepted")["requestStatus"],202)
    def test_requestStatus(self): 
        self.assertEqual(numberReposandCommits("checkOnStatusCode 302 Found")["requestStatus"],302)
    def test_requestStatus(self): 
        self.assertEqual(numberReposandCommits("checkOnStatusCode 304 Not Modified")["requestStatus"],304)
    def test_requestStatus(self): 
        self.assertEqual(numberReposandCommits("checkOnStatusCode 400 Bad Request")["requestStatus"],400)
    def test_requestStatus(self): 
        self.assertEqual(numberReposandCommits("checkOnStatusCode 404 Not Found")["requestStatus"],404)
    def test_requestStatus(self): 
        self.assertEqual(numberReposandCommits("checkOnStatusCode 500 Internal Server Error")["requestStatus"],500)
    def test_requestStatus(self): 
        self.assertEqual(numberReposandCommits("checkOnStatusCode 503 Service Unavailable")["requestStatus"],503)

if __name__ == '__main__':
    print('       unit tests  ....  ')
    unittest.main(exit=False)
