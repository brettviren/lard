#!/usr/bin/env python
'''The lard data model.

The objects in this module make up an internal, transient data schema.

Modules under lard.adapters produce this data model and modules under
lard.renderers accept it to produce some end form.

'''

from collections import namedtuple

ScalarPoint = namedtuple('ScalarPoint', 'x y z s')
def CastScalarPoint(d):
    if type(d) == dict:
        return ScalarPoint(float(d['x']),float(d['y']),float(d['z']),float(d['s']))
    if type(d) == tuple or type(d) == list:
        return ScalarPoint(float(d[0]),float(d[1]),float(d[2]),float(d[3]))
    return ScalarPoint(float(d.x),float(d.y),float(d.z),float(d.s))

#from schema import Schema, Use, Optional
from voluptuous import Schema, Optional
# schema v1 is a pair of lists of scalar point values, for simulation "truth" and reconstructed.
schema_v1 = Schema(
    {
        Optional('truth'): [CastScalarPoint],
        Optional('recon'): [CastScalarPoint],
    }
)

# Most recent version
schema = schema_v1

def validate(data, version=None):
    'Validate data against schema'
    if version is None:
        return schema(data)
    if version == 'v1' or version == 1:
        return schema_v1(data)
    return version(data) # assume version is a Schema object
