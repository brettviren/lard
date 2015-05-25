#!/usr/bin/env python

import json        

def render(data, mime, **opts):
    '''
    Render for wire-cell-3dvis
    '''
    x=list()
    y=list()
    z=list()
    for p in data['truth']:
        x.append(p.x)
        y.append(p.y)
        z.append(p.z)
    return json.dumps(dict(x=x,y=y,z=z))
    
def accept(mime, **opts):
    '''
    Return true if this module's render method accepts the mime type
    '''
    if not mime.startswith('application/wc3dvis'):
        return 
    ver = opts.get("version", '2.0')
    if ver == '2.0':
        return lambda d: render(d, mime, **opts)
    return lambda d, r: render(d, r, mime, **opts)
