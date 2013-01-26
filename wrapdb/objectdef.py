# objectdef.py

from urllib2 import Request, urlopen
import simplejson as json

from wrapdb import utils

PROJECT_URL = '/objects/create'

def create(apiKey, objectDefName, objectDef):
    data = json.dumps(objectDef)
    params = 'api_key=%s&name=%s' % (apiKey, objectDefName)
    url = utils.get_url(PROJECT_URL, params)

    request = Request(url, data, {'Content-Type': 'application/json'})
    return json.load(urlopen(request))
