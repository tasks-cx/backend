from flask import make_response
from datetime import datetime

try:
    import simplejson as json
except ImportError:
    try:
        import json
    except ImportError:
        raise ImportError

class JSONEncoder(json.JSONEncoder):

    def default(self, o):
        global jsonParsingParam
        if getattr(o, 'to_json', None):
            return json.loads(o.to_json())
        if isinstance(o, datetime.datetime):
            return o.strftime("%Y-%m-%dT%H:%I:%S%z")
        return json.JSONEncoder.default(self, o)

def jsonify(args):
    global jsonParsingParam
    response = make_response(json.dumps(
        args, cls=JSONEncoder, **jsonParsingParam))
    response.headers.set('Content-Type', "application/json")
    return response
