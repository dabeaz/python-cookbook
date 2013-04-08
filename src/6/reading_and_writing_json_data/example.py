# Some advanced JSON examples involving ordered dicts and classes
import json

# Some JSON encoded text
s = '{"name": "ACME", "shares": 50, "price": 490.1}'

# (a) Turning JSON into an OrderedDict

from collections import OrderedDict
data = json.loads(s, object_pairs_hook=OrderedDict)
print(data)

# (b) Using JSON to populate an instance

class JSONObject:
    def __init__(self, d):
        self.__dict__ = d

data = json.loads(s, object_hook=JSONObject)
print(data.name)
print(data.shares)
print(data.price)

# (c) Encoding instances

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def serialize_instance(obj):
    d = { '__classname__' : type(obj).__name__ }
    d.update(vars(obj))
    return d

p = Point(3,4)
s = json.dumps(p, default=serialize_instance)
print(s)

# (d) Decoding instances
classes = {
    'Point' : Point
}

def unserialize_object(d):
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls)
        for key, value in d.items():
            setattr(obj, key, value)
        return obj
    else:
        return d

a = json.loads(s, object_hook=unserialize_object)
print(a)
print(a.x)
print(a.y)

            
