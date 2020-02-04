from mrjob.job import MRJob
import random

class MRMultilineInput(MRJob):               
    def mapper_init(self):
        self.message_id = ''
        self.in_body = False
        self.body = []
    
    def mapper(self, _, line):
        line = line.strip()
        if line.find('Message-ID:') == 0:
            self.message_id = line[13:len(line)-1]
            
        if not line and not self.in_body:
            self.in_body=True
        
        if line.find('From general') == 0 and self.in_body:
            yield self.message_id, ''.join(self.body)
            self.message_id = ''
            self.body = []    
            self.in_body = False
        
        if self.in_body:
            self.body.append(line)
                       
if __name__ == '__main__':
    MRMultilineInput.run()