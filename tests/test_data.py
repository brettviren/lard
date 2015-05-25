#!/usr/bin/env python
'''
Test lard.data
'''

import lard.data
from lard.data import ScalarPoint as SP


def test_schema():
    d = dict(truth = [[1.0,2.0,3.0,0.0], SP(10.0,20.0,30.0,'100.0')],
             recon = [(1.1,2.2,3.3,0.1), SP(11.0,21.0,'31',101)])
    res = lard.data.validate(d)
    print res
    assert res

def test_optional():
    d = dict(recon = [(1.1,2.2,3.3,0.1), SP(11.0,21.0,'31',101)])
    res = lard.data.validate(d)
    print res
    assert res


