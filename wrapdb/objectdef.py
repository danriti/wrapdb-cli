# objectdef.py

from urllib2 import Request, urlopen
import simplejson as json

from wrapdb import utils

def create(apiKey, objectDefName, objectDef):
    data = json.dumps(objectDef)
    params = 'api_key=%s&name=%s' % (apiKey, objectDefName)
    url = utils.get_url('objects/create', params)

    request = Request(url, data, {'Content-Type': 'application/json'})
    return json.load(urlopen(request))

def get(apiKey):
    params = 'api_key=%s' % (apiKey)
    url = utils.get_url('objects/get', params)
    return json.load(urlopen(url))
