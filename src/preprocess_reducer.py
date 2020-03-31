#!/usr/bin/env python

import sys

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
    print(line)
    