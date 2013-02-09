#!/usr/bin/python

from urllib2 import urlopen
import random
import simplejson
import string
import unittest

from wrapdb import endpoint, instance, objectdef, project, utils

API_KEY = '123Key'

# Returns a randomly generated 6 character string.
def get_random_string():
    return ''.join(random.choice(string.ascii_uppercase + 
                                 string.digits) for x in range(6)) 

# Test Cases!
class WrapDBTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_server_response(self):
        response = simplejson.load(urlopen(utils.get_url('test')))
        self.assertEqual(response.get('status'), 'success')

    def test_create_project(self):
        response = project.create(API_KEY, get_random_string())
        self.assertEqual(response.get('status'), 'success')

    def test_get_projects(self):
        response = project.create(API_KEY, get_random_string())
        response = project.create(API_KEY, get_random_string())

        # Fail to get projects due to invalid api key.
        response = project.get('invalid_key')
        self.assertEqual(response.get('status'), 'fail')

        response = project.get(API_KEY)
        projects = response.get('projects')
        self.assertEqual(response.get('status'), 'success')
        self.assertTrue(len(projects) > 2)

    def test_create_objectdef(self):
        objectDefData = {'data' : [{'name' : 'first_name', 'type' : 'string'},
                                   {'name' : 'last_name', 'type' : 'string'}]}

        response = objectdef.create(API_KEY, 'person', objectDefData)
        self.assertEqual(response.get('status'), 'success')

    def test_get_objectdef(self):
        objectDefData = {'data' : [{'name' : 'name', 'type' : 'string'},
                                   {'name' : 'rating', 'type' : 'string'},
                                   {'name' : 'cuisine', 'type' : 'string'}]}

        response = objectdef.create(API_KEY, 'restaurant', objectDefData)
        response = objectdef.get(API_KEY)
        objects =  response.get('objects')
        self.assertEqual(response.get('status'), 'success')
        self.assertTrue(objects > 1)

    # Test create and get of endpoints.
    def test_endpoints(self):
        response = project.create(API_KEY, get_random_string())
        projectId = response.get('id')
        endpointName = get_random_string()
        endpointData = {'data' : [{                                       
                                      'name' : 'title',                  
                                      'type' : 'string',                 
                                      'value' : 'MyBathrooms'            
                                  },
                                  {                                       
                                      'name' : 'message',                  
                                      'type' : 'string',                 
                                      'value' : 'Hello world!'            
                                  }]       
                       }

        # Fail due to invalid api key.
        response = endpoint.create('invalid_key', projectId, endpointName, endpointData)
        self.assertEqual(response.get('status'), 'fail')

        # Fail due to invalid project id.
        response = endpoint.create(API_KEY, 'invalid_project', endpointName, endpointData)
        self.assertEqual(response.get('status'), 'fail')

        # Successfully create a project endpoint!
        response = endpoint.create(API_KEY, projectId, endpointName, endpointData)
        self.assertEqual(response.get('status'), 'success')

        # Fail due to invalid api key.
        response = endpoint.get('invalid_key', projectId)
        self.assertEqual(response.get('status'), 'fail')

        # Fail due to invalid project id.
        response = endpoint.get(API_KEY, 'invalid_project')
        self.assertEqual(response.get('status'), 'fail')

        # Successfully get a list of endpoints.
        response = endpoint.get(API_KEY, projectId)
        endpoints = response.get('endpoints')
        self.assertEqual(response.get('status'), 'success')
        self.assertTrue(len(endpoints) > 0)

    def test_krapp(self):
        # You can't have duplicate project names in WrapDB. So to make it easier
        # to rerun tests, just generate a random project name.
        projectName = get_random_string()

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
