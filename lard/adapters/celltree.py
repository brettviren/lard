#!/usr/bin/env python

from lard.root import TreeReader

def convert(path, record=0, **args):
    '''
    Return the data for the record of a celltree file of the given path
    '''
    reader = TreeReader(path, 'Event/Sim')
    rec = reader[record]
    truth = list()
    for ind in range(int(rec.simide_size)):
        truth.append((rec.simide_x.at(ind),
                      rec.simide_y.at(ind),
                      rec.simide_y.at(ind),
                      rec.simide_numElectrons.at(ind)))
    return dict(truth = truth)

