#!/usr/bin/env python

import sys
import pickle

MUNICIPALITIES_TO_MODERN = {}
BIRTH_PLACE_REPLACE = {}
RELIGION_REPLACE = {}

with open('./data.p', "rb") as f:
    MUNICIPALITIES_TO_MODERN, BIRTH_PLACE_REPLACE, RELIGION_REPLACE = pickle.load(f)

def findUpdatedBirthPlace(a):
    a = str(a).strip().title()
    if a in BIRTH_PLACE_REPLACE:
        a = BIRTH_PLACE_REPLACE[a]
    else:
        a = ' '.join([(BIRTH_PLACE_REPLACE[w] if w in BIRTH_PLACE_REPLACE else w) for w in a.split()]) # Do some typo and abbrevation fixup.

    a = a.replace('aa','å').replace('Aa','Å')
    candidates = [MUNICIPALITIES_TO_MODERN[w] for w in a.split() if w in MUNICIPALITIES_TO_MODERN] # A list of birth places that have a matching municipality.
    return (candidates[0] if (len(candidates) > 0) else a) # If there is a candidate, just pick the first one for now.

def cleanupFieldOfWork(r):
    if 'fisker' in r:
        return 'Fisher'
    
    if 'hustru' in r:
        return 'Housewife'
    
    if 'gaard' in r:
        return 'Farmer'
    
    if 'tjenestep' in r:
        return 'Maid'
    
    return r.title()

def cleanupReligion(r):
    if r in RELIGION_REPLACE:
        return RELIGION_REPLACE[r]
    
    if 'Luthersk' in r or 'Lutersk' in r or 'Luth' in r or 'Lutheraner' in r:
        return 'Lutheranism'
    
    if 'Methodist' in r or 'Metodist' in r:
        return 'Methodism'
    
    if 'Adventist' in r:
        return 'Adventism'
    
    if 'Katholsk' in r or 'Katolik' in r or 'Katolsk' in r:
        return 'Catholism'
    
    if 'Frimenig' in r or 'Frikirke' in r:
        return 'Evangelical Lutheran Free Church'
    
    if 'Kristi' in r:
        return 'Kristi Menighet'
    
    if 'Mormon' in r:
        return 'Mormon'
    
    if 'Mosaisk' in r:
        return 'Jew'
    
    if 'Dissenter' in r or 'Desenter' in r or 'Disenter' in r:
        return 'Dissenter'
    
    if 'Samfundet' in r or 'samfundet' in r:
        return 'Quakers'
    
    return r.title()

# INDEXES
# 0 - Census Year
# 1 - County
# 2 - Municipality
# 3 - Gender
# 4 - Field of Work
# 5 - Martial Status
# 6 - Religion/Faith
# 7 - Birth Year
# 8 - Birth Place (Municipality)

#sys.stdin.reconfigure(encoding='utf-8') # Ensure correct encoding.

for line in sys.stdin:
    line = line.strip()
    try:
        line = [str(string) for string in line.split(',')]
    except:
        continue

    if len(line) < 9: # Bogus, skip!
        continue

    # Update municipality name to todays municipality name.
    line[2] = MUNICIPALITIES_TO_MODERN[line[2]]
    
    # Preprocess birthplaces and find the 'todays' municipality from the preprocessed birth place.
    line[-1] = findUpdatedBirthPlace(line[-1])

    # Preprocess field of work.
    # Fix typos and casings.
    line[4] = cleanupFieldOfWork(line[4].lower())

    # Preprocess religion.
    # Fix faulty abbrevations and typos.
    line[6] = cleanupReligion(line[6])

    print("".join(line[2:]))
