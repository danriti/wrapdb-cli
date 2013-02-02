#!/usr/bin/python

from urllib2 import urlopen
import random
import simplejson
import string
import unittest

from wrapdb import instance, objectdef, project, utils

API_KEY = '123Key'

# Test Cases!
class WrapDBTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_server_response(self):
        response = simplejson.load(urlopen(utils.get_url('test')))
        self.assertEqual(response.get('status'), 'success')

    def test_create_project(self):
        response = project.create(API_KEY, "Testing123")
        self.assertEqual(response.get('status'), 'success')

    def test_create_objectdef(self):
        objectDefData = {'data' : [{'name' : 'name', 'type' : 'string'},
                                   {'name' : 'address', 'type' : 'string'}]}

        response = objectdef.create(API_KEY, 'business', objectDefData)
        self.assertEqual(response.get('status'), 'success')

    def test_krapp(self):
        # You can't have duplicate project names in WrapDB. So to make it easier
        # to rerun tests, just generate a random project name.
        projectName = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(6))

        # Create project.
        response = project.create(API_KEY, projectName)
        self.assertEqual(response.get('status'), 'success')

        # Grab the project id.
        projectId = response.get('id')

        # Setup business object definition name and data.
        objectDefName = 'business'
        objectDefData = {'data' : [{'name' : 'name', 'type' : 'string'},
                                   {'name' : 'address', 'type' : 'string'}]}

        # Create business object.
        response = objectdef.create(API_KEY, objectDefName, objectDefData)
        self.assertEqual(response.get('status'), 'success')

        # Setup business object instance.
        instanceData = {'data' : {"name" : "McDonalds",
                                  "address" : "123 Happy Meal St"}}

        # Fail insertion of object due to invalid project id.
        response = instance.insert(API_KEY,
                                   "invalid_project_id",
                                   objectDefName,
                                   instanceData)
        self.assertEqual(response.get('status'), 'fail')

        # Fail insertion of object due to invalid api key.
        response = instance.insert("invalid_api_key",
                                   projectId,
                                   objectDefName,
                                   instanceData)
        self.assertEqual(response.get('status'), 'fail')

        # Insert a business object.
        response = instance.insert(API_KEY,
                                   projectId,
                                   objectDefName,
                                   instanceData)
        self.assertEqual(response.get('status'), 'success')

# Get going test runner!
if __name__ == '__main__':
    unittest.main()
