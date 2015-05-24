#!/usr/bin/env python
'''
Interface to ROOT
'''

import ROOT

def open_file(filename):
    '''
    Return an open ROOT.TFile on the given filename
    '''
    return ROOT.TFile.Open(filename)



def leaves(tree):
    '''
    Return a sequence of leaves in the tree.
    '''
    for branch in tree.GetListOfBranches():
        for leaf in branch.GetListOfLeaves():
            yield leaf



class TreeReader(object):
    def __init__(self, filename, treepath):
        self._tfile = open_file(filename)
        self._tree = self._tfile.Get(treepath)
        self._reader = ROOT.TTreeReader(self._tree)
        
        self.leaf = dict()
        for leaf in leaves(self._tree):
            TTRVClass = ROOT.TTreeReaderValue(leaf.GetTypeName())
            leaf_name = leaf.GetName()
            self.leaf[leaf_name] = TTRVClass(self._reader, leaf_name)

    def __getattr__(self, name):
        return self.leaf[name]

    def __iter__(self):
        return self
    def next(self):
        ret = self._reader.Next()
        if not ret:
            raise StopIteration
        return ret
