# project.py

from urllib2 import urlopen
import simplejson

from wrapdb import utils

PROJECT_URL = 'projects/'

def create(name):
    url = utils.get_url('projects/create', 'name=' + name)
    return simplejson.load(urlopen(url))
