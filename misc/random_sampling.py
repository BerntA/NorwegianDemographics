from mrjob.job import MRJob
import random

class MRRandomSampling(MRJob):
                   
    def configure_options(self):
        super(MRRandomSampling, self).configure_options()
        self.add_passthrough_option('--samplingRate', type='float', default=.1)
        self.add_passthrough_option('--seed', type='float', default=10)
                  
    def mapper_init(self):
        random.seed(self.options.seed)
        
    def mapper(self, _, line):
        line = line.strip()
        if line.find('Subject:') == 0:
            if random.random()<self.options.samplingRate:
                yield _, line[9:]
                
if __name__ == '__main__':
    MRRandomSampling.run()