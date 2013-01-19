HOST = 'http://localhost:3000/'

# Helper methods!
def get_url(endpoint, params=''):
    return HOST + endpoint + '?api_key=123Key&session_token=123Session&' + params
