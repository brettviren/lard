#!/usr/bin/env python
'''Supported data adapters.

These should present the "lard" data model in a Python data structure
representation of whatever data source they adapt.

Each adapter is a callable called like:

  module.adapt(path, record) -> data structure passing lard.data.validate()

'''

import celltree

__all__ = ['celltree']
