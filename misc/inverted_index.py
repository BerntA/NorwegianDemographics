from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import JSONProtocol

class MRInvertedIndex(MRJob):
    INPUT_PROTOCOL = JSONProtocol
    
    def mapper(self, email_id, email_body):
        for word in email_body.split():
            if email_id:
                yield word, email_id
                
    def combiner(self, word, email_ids):
        email_ids_set = set(email_ids)
        for email_id in email_ids_set:
            yield word, email_id
                    
    def reducer(self, word, email_ids):
        email_ids_list = list(set(email_ids))
        yield word, (len(email_ids_list),email_ids_list)

if __name__ == '__main__':
    MRInvertedIndex.run()