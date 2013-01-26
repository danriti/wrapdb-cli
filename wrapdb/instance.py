# instance.py

from urllib2 import Request, urlopen
import simplejson as json

from wrapdb import utils

PROJECT_URL = '/%s/%s/insert'

def insert(apiKey, projectId, objectDefName, instanceData):
    data = json.dumps(instanceData)
    params = 'api_key=%s' % (apiKey)
    url = utils.get_url(PROJECT_URL % (projectId, objectDefName.lower()),
                        params)

    request = Request(url, data, {'Content-Type': 'application/json'})
    return json.load(urlopen(request))
