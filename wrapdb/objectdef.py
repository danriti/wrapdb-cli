# objectdef.py

from urllib2 import Request, urlopen
import simplejson as json

from wrapdb import utils

PROJECT_URL = '/objects/create'

def create(username, objectDefName, objectDef):
    data = json.dumps(objectDef)
    url = utils.get_url(username + PROJECT_URL, 'name=' + objectDefName)
    request = Request(url, data, {'Content-Type': 'application/json'})
    return json.load(urlopen(request))
