#!/usr/bin/python

from urllib2 import urlopen
import simplejson
import unittest

from wrapdb import project, utils

# Test Cases!
class WrapDBTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_server_response(self):
        response = simplejson.load(urlopen(utils.get_url('test')))
        self.assertEqual(response.get('status'), 'success')

    def test_create_project_pass(self):
        response = project.create("Krapp")
        self.assertEqual(response.get('status'), 'success')
        
# Get going test runner!
if __name__ == '__main__':
    unittest.main()
