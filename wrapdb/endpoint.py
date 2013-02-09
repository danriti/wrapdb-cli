# endpoint.py

from urllib2 import Request, urlopen
import simplejson as json

from wrapdb import utils

def create(apiKey, projectId, endpointName, endpointData):
    data = json.dumps(endpointData)
    params = 'api_key=%s&name=%s' % (apiKey, endpointName)
    url = utils.get_url('%s/endpoints/create' % (projectId), params)

    request = Request(url, data, {'Content-Type': 'application/json'})
    return json.load(urlopen(request))

def get(apiKey, projectId):
    params = 'api_key=%s' % (apiKey)
    url = utils.get_url('%s/endpoints/get' % (projectId), params)
    return json.load(urlopen(url))
