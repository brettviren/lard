#!/usr/bin/env python
'''This is the lard server.

The CONTENT_TYPE should specify a MIME type and version that specifies
the format and schema that the served data shall follow.  The URL is
composed of a data source and a file.

  /source/filename

Optional POST parameters can be specified:

  record=<int> : specify the record 0-indexed number ("event") to return
  
'''
# curl -H "Content-type: application/wc3dvis+json;version=2.0" \
#      -X POST http://localhost:8899/root/test.root -d '{"foo":"bar"}'



import lard.adapters
import lard.data
from lard.renderers import renderer

from flask import Flask, request
app = Flask('lard')

from werkzeug.http import parse_options_header

import logging
file_handler = logging.FileHandler('lard.log')
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)

@app.route('/')
def api_root():
    return 'Welcome'

@app.route('/<adapter>/<path:path>', methods=['GET','POST'])
def api_frontend_adapter(adapter, path):
    ct = parse_options_header(request.headers.get('Content-Type'))
    render = renderer(ct)

    mod = getattr(lard.adapters, adapter)
    data = mod.convert(path, **request.args)
    data = lard.data.validate(data)
    return render(data)



if '__main__' == __name__:
    app.run(port=8899)
