#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import csv

SS_CSV_ENCODING = 'cp1252'

def get_reader(filename, encoding=SS_CSV_ENCODING):
    with open(filename, encoding=encoding, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row
            
