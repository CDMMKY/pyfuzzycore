# -*- coding: utf-8 -*-

from collections import OrderedDict


def parse_file(path):
    attributes = OrderedDict()
    X = []
    y = []
    with open(path, 'r') as trn:
        data_name = get_data_name(trn.readline().rstrip('\n'))
        line = trn.readline().rstrip('\n')
        while line.startswith('@attribute'):
            name, domain = line.split(' ')[1:]
            if name != 'Class':
                domain = tuple(map(float, 
                                   domain[:-1].split('[')[1].split(',')))
                attributes[name] = domain
            else:
                classes = tuple(domain[1:-1].split(','))
            line = trn.readline().rstrip('\n')
        while not line.startswith('@data'):
            line = trn.readline()
        for line in trn:
            data = line.rstrip('\n').split(',')
            X.append(list(map(float, data[:-1])))
            y.append(data[-1])
        return(data_name, attributes, classes, X, y)
        

def get_data_name(line):
    if line.startswith('@relation'):
        data_name = line.split(' ')[1]
    else:
        print('Incorrect header - no @relation param')
        return
    return data_name
