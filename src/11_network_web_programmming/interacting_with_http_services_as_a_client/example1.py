# A basic GET request

from urllib import request, parse

# Base URL being accessed 
url = 'http://httpbin.org/get'

# Dictionary of query parameters (if any)
parms = {
   'name1' : 'value1',
   'name2' : 'value2'
}

# Encode the query string
querystring = parse.urlencode(parms)

# Make a GET request and read the response
u = request.urlopen(url+'?' + querystring)
resp = u.read()

import json
from pprint import pprint

json_resp = json.loads(resp.decode('utf-8'))
pprint(json_resp)

