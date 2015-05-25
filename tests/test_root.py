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
test_root_http_url = "http://www.phy.bnl.gov/~chao/wire-cell-events/2.0/celltree_muon_1.5GeV_30x30deg.root"

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

    TTreeReaderValueInt = ROOT.TTreeReaderValue('int')
    siz = TTreeReaderValueInt(reader, "simide_size")
    TTreeReaderValueVectorInt = ROOT.TTreeReaderValue('std::vector<int>')
    chid = TTreeReaderValueVectorInt(reader, "calib_channelId")
    while (reader.Next()):
        assert siz
        assert chid
        print int(siz), chid.size()

def dump_reader(reader):
    simsiz = int(reader.simide_size)
    chid = reader.calib_channelId
    print '#chan IDs=%d, simid siz=%d' % (chid.size(), simsiz)
    chids = [chid.at(i) for i in range(chid.size())]
    assert len(chids) == chid.size()

def spin_reader(reader):
    for siz in reader:
        assert siz
        dump_reader(reader)

def test_tree_reader():
    'Test lard.root.TreeReader'
    reader = lard.root.TreeReader(test_root_filename, test_root_treepath)
    spin_reader(reader)

def test_remote_root():
    'Test lard.root.TreeReader with a remote file'
    reader = lard.root.TreeReader(test_root_http_url, test_root_treepath)
    spin_reader(reader)

def test_indexing():
    reader = lard.root.TreeReader(test_root_filename, test_root_treepath)
    for ind in range(5):
        dump_reader(reader[ind])
