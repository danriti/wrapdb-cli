# project.py

from urllib2 import urlopen
import simplejson

from wrapdb import utils

PROJECT_URL = 'projects/'

def create(apiKey, projectName):
    params = 'api_key=%s&name=%s' % (apiKey, projectName)
    url = utils.get_url('projects/create', params)
    return simplejson.load(urlopen(url))
