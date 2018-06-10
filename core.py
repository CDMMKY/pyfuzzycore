# -*- coding: utf-8 -*-

import os
from keel.parser import parse_file


def process(data_folder, rules_generator=None, tune_method=None):
    if os.path.exists(data_folder):
        files = os.listdir(data_folder)
    else:
        return
    for file in files:
        *_, X, y = parse_file(os.path.join(data_folder, file))
        print(len(X), len(y))
