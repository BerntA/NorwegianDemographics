#!/usr/bin/env python

import sys

for line in sys.stdin: # read input from STDIN
  line = line.strip() # remove leading and trailing whitespace
  if line.find("From:") == 0:
    email_domain = line[line.find("@")+1:line.find(">")]
    if len(email_domain) == 0:
      email_domain == "empty"
    print '%s\t%s' % (email_domain, 1) # print output to STDOUT tab delimited