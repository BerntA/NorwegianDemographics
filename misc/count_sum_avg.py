from mrjob.job import MRJob
from mrjob.step import MRStep

class MRCountSumAvg(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_count,
                   combiner=self.combiner_count,
                   reducer=self.reducer_count),
            MRStep(mapper=self.mapper_avg,
                   reducer=self.reducer_avg)
            ]

    def mapper_count(self, _, line):
        line = line.strip()
        if line.find('From:') == 0:
            email_domain = line[line.find('@')+1:line.find('>')]
            if len(email_domain) == 0:
                email_domain == 'empty'
            yield email_domain, 1

    def combiner_count(self, key, values):
        yield key, sum(values)
        
    def reducer_count(self, key, values):
        yield key, sum(values)
        
    def mapper_avg(self, key, value):
        yield 'amount', value

    def reducer_avg(self, key, values):
        values_list = list(values)
        yield 'avg emails per domain', sum(values_list)/len(values_list)
        yield 'max emails per domain', max(values_list)
        yield 'min emails per domain', min(values_list)

if __name__ == '__main__':
    MRCountSumAvg.run()