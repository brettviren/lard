#!/usr/bin/env python
'''
Test lard.root
'''

import os
import lard.root
ROOT = lard.root.ROOT

testdir = os.path.dirname(os.path.realpath(__file__))
test_root_filename = os.path.join(testdir, "test.root")
test_root_treepath = "Event/Sim"

def get_test_file():
    tfile = lard.root.open_file(test_root_filename)
    assert tfile
    return tfile

def test_leaves():
    'Test lard.root.leaves()'
 
    tfile = get_test_file()
    tree = tfile.Get(test_root_treepath)
    assert tree

    for leaf in lard.root.leaves(tree):
        assert leaf
        print leaf.GetName(), leaf.GetOffset(), leaf.GetTypeName()

def test_reader():
    'Test reader concepts'
    tfile = get_test_file()
    tree = tfile.Get("Event/Sim")
    reader = ROOT.TTreeReader(tree)
    TTreeReaderValueVectorInt = ROOT.TTreeReaderValue('std::vector<int>')
    chid = TTreeReaderValueVectorInt(reader, "calib_channelId")
    while (reader.Next()):
        assert chid
        print chid.size()


def test_tree_reader():
    'Test lard.root.TreeReader'
    reader = lard.root.TreeReader(test_root_filename, test_root_treepath)
    for siz in reader:
        chid = reader.calib_channelId
        print '[%d] #chan IDs=%d' % (siz, chid.size())
        chids = [chid.at(i) for i in range(chid.size())]
        assert len(chids) == chid.size()
