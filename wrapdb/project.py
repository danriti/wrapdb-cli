# project.py

from urllib2 import urlopen
import simplejson

from wrapdb import utils

def create(apiKey, projectName):
    params = 'api_key=%s&name=%s' % (apiKey, projectName)
    url = utils.get_url('projects/create', params)
    return simplejson.load(urlopen(url))

def get(apiKey):
    params = 'api_key=%s' % (apiKey)
    url = utils.get_url('projects/get', params)
    return simplejson.load(urlopen(url))
