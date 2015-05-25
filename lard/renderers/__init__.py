#!/usr/bin/env python
'''
Renders of lard data
'''
import wc3dvis

modules = [wc3dvis]


def renderer(content_types):
    mime, opts = content_types
    for mod in modules:
        maybe = mod.accept(mime, **opts)
        if maybe:
            return maybe
