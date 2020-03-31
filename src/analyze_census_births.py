#!/usr/bin/python3

import sys
from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import RawProtocol, BytesValueProtocol, RawValueProtocol, JSONValueProtocol

class MRAnalyzeBirths(MRJob):

    #INPUT_PROTOCOL = RawValueProtocol
    #INTERNAL_PROTOCOL = RawValueProtocol
    #OUTPUT_PROTOCOL = JSONValueProtocol

    def steps(self):
        return [
            # MRStep(mapper=self.mapper_count,
            #        combiner=self.combiner_count,
            #        reducer=self.reducer_count),
            MRStep(mapper=self.mapper_births,
                   reducer=self.reducer_births)
            ]

    def mapper_births(self, k, v):
        line = v.strip().split(',')
        yield (line[-2], line[-1]), 1

    def reducer_births(self, k, v):
        data = list(v)
        yield k, len(data)

if __name__ == '__main__':
    MRAnalyzeBirths.run()