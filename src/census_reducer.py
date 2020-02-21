#!/usr/bin/env python

from operator import itemgetter
import sys

data = {}

for line in sys.stdin:
    line = line.strip()
    try:
        bosted, fodt, kjonn, fodested = line.split('@', 3)
    except:
        print("error:", line)
        continue
    
    currPlace = fodested if len(fodested) > 1 else bosted
    if currPlace in data:
        data[currPlace][str(fodt)] = int(data[currPlace].get(str(fodt), 0)) + 1
    else:
        data[currPlace] = {}
        data[currPlace][str(fodt)] = 1

for place, vals in data.items():
    for year, cnt in vals.items():
        print('{}\t{}\t{}'.format(year, place, cnt))