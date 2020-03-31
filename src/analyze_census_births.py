#!/usr/bin/python3

from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import RawProtocol, BytesValueProtocol, RawValueProtocol, JSONValueProtocol

class CSVProtocol(object):

    def read(self, line):
        d = line.split(',')
        return (d[0], d[1]), int(d[2])

    def write(self, key, value):
        return '{},{},{}'.format(key[0], key[1], value).encode()

class MRAnalyzeBirths(MRJob):

    #INPUT_PROTOCOL = XYZ
    #INTERNAL_PROTOCOL = XYZ
    OUTPUT_PROTOCOL = CSVProtocol # Produce output as CSV so that we can load the results directly in our visualization notebook.

    def steps(self):
        return [
                MRStep(mapper=self.mapper_births, reducer=self.reducer_births)
            ]

    def mapper_births(self, k, v):
        line = v.strip().split(',')
        yield (line[-2], line[-1]), 1

    def reducer_births(self, k, v):
        data = list(v)
        yield k, len(data)

if __name__ == '__main__':
    MRAnalyzeBirths.run()
    