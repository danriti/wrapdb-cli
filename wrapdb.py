#!/usr/bin/python

from urllib2 import urlopen
import simplejson
import unittest

HOST = "http://localhost:3000/"

# Helper methods!
def get_url(endpoint):
    return HOST + endpoint

# Test Cases!
class WrapDBTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_server_response(self):
        response = simplejson.load(urlopen(get_url("test")))
        self.assertEqual(response.get('success'), "ok")

# Get going test runner!
if __name__ == "__main__":
    unittest.main()
