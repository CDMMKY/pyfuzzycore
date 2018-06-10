# -*- coding: utf-8 -*-

import os
from keel.parser import parse_file


def process(data_folder, rules_generator=None, tune_method=None):
    if os.path.exists(data_folder):
        files = os.listdir(data_folder)
        pairs = [files[i:i+2] for i in range(0, len(files), 2)]
        print(pairs)
    else:
        return
    for trn, tst in pairs:
        *_, X_trn, y_trn = parse_file(os.path.join(data_folder, trn))
        *_, X_tst, y_tst = parse_file(os.path.join(data_folder, tst))
        print(len(X_trn), len(X_tst), len(y_trn), len(y_tst))
        #rules = rules_generator(X_trn, y_trn)
        #learn, test = tune_method(rules, X_trn, y_trn, X_tst, y_tst)
        #print(learn, test)
