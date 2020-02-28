#!/usr/bin/env python

import sys
import codecs

person, bosted, fodested, fodeaar, kjonn = False, '?', '?', '?', '?'
for line in sys.stdin:
    line = line.strip() # remove leading and trailing whitespace
    sted_start, sted_end = line.find("<bostedets_navn>"), line.find("</bostedets_navn>")
    if sted_start >= 0:
        bosted = line[(sted_start+16):sted_end]

    if not person:
        if line.find("<person") >= 0:
            person = True
            fodested = fodeaar = kjonn = '?'
    else:
        # We reached the end for this person, reset.
        if line.find("</person>") >= 0:
            person = False
            print("{}@{}@{}@{}".format(bosted,fodeaar,kjonn,fodested))
            continue

        k = line.find("<kjonn>")
        if k >= 0:
            kjonn = line[(k+7):(k+8)]

        aar_start, aar_end = line.find(">"), line.find("</fodselsaar>")
        if aar_end >= 0:
            fodeaar = line[(aar_start+1):aar_end][:4]

        sted_start, sted_end = line.find("<fodested>"), line.find("</fodested>")
        if sted_start >= 0:
            fodested = line[(sted_start+10):sted_end]