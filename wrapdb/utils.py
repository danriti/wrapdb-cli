HOST = 'http://localhost:3000/'

# Helper methods!
def get_url(endpoint, params=''):
    return HOST + endpoint + '?session_token=123Session&' + params
