#!/usr/bin/python3

from mrjob.job import MRJob

class CSVProtocol(object):

    def read(self, line):
        d = line.split(',')
        return d[0], int(d[1])

    def write(self, key, value):
        return '{},{}'.format(key, value).encode()

class MRAnalyzeBirths(MRJob):

    OUTPUT_PROTOCOL = CSVProtocol # Produce output as CSV so that we can load the results directly in our visualization notebook.

    def mapper(self, k, v):
        line = v.strip().split(',')
        yield line[0], 1

    def reducer(self, k, v):
        data = list(v)
        yield k, sum(data)

if __name__ == '__main__':
    MRAnalyzeBirths.run()
    