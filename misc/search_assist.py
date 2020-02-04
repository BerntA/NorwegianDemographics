from mrjob.job import MRJob
from mrjob.step import MRStep

class MRSearchAssist(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_count,
                   combiner=self.combiner_count,
                   reducer=self.reducer_count),
            MRStep(mapper=self.mapper_trans,
                   reducer=self.reducer_trans)
                   ]   

    def mapper_count(self, _, line):
        line = line.strip()
        if line.find('Subject:') == 0:
            linel = line[9:].split()
            pairs = zip(linel, linel[1:])
            for pair in pairs:
                yield pair, 1

    def combiner_count(self, pair, count):
        yield pair, sum(count)
        
    def reducer_count(self, pair, count):
        yield pair, sum(count)
        
    def mapper_trans(self, pair, count):
        first = pair[0]
        second = pair[1]
        yield first, (second, count)
    
    def reducer_trans(self, word, second_list):
        sorted_list = sorted(list(second_list), key = lambda second: -second[1])
        if len(sorted_list)>=3:
            yield word, [second for (second, count) in sorted_list[:3]]
        
        
if __name__ == '__main__':
    MRSearchAssist.run()