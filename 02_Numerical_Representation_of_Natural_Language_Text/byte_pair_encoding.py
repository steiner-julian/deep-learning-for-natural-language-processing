from vocabulary import Vocabulary
from corpus import HuggingFaceCorpus, SlideExampleCorpus

class BytePairEncoding:
    def __init__(self, vocabulary : Vocabulary, k : int):
        self.tokens = []
        self.vocabulary = vocabulary
        self.k = k
    
    def _compute_pair_frequencies(self):
        pairs = self._compute_pairs_from_vocabulary()

        pair_frequencies = {}

        for pair in pairs:
            if pair in pair_frequencies.keys():
                pair_frequencies[pair] += 1
            else:
                pair_frequencies[pair] = 1
        
        return pair_frequencies
    
    def _compute_pairs_from_vocabulary(self):
        pairs = []

        for i, j in zip(range(len(self.vocabulary)-1), range(1, len(self.vocabulary))):
            if self.vocabulary[i] == '_' or self.vocabulary[j] == '_': continue
            pairs.append((self.vocabulary[i], self.vocabulary[j]))
        
        return pairs

    def _merge_pairs(self, max_pair_frequency):
        voc = []

        skip_next = False

        for i, j in zip(range(len(self.vocabulary)-1), range(1, len(self.vocabulary))):

            if skip_next:
                skip_next = False
                continue

            if (self.vocabulary[i], self.vocabulary[j]) == max_pair_frequency:
                voc.append(f'{self.vocabulary[i]}{self.vocabulary[j]}')
                skip_next = True
            else:
                voc.append(self.vocabulary[i])
                skip_next = False
            
            if j+1 == len(self.vocabulary):
                voc.append(self.vocabulary[j])
        
        self.vocabulary = voc
    
    def encoding(self):
        for _ in range(self.k):
            pair_frequencies = self._compute_pair_frequencies()
            max_pair_frequency = max(pair_frequencies, key=pair_frequencies.get)
            self._merge_pairs(max_pair_frequency)
        
        return set(self.vocabulary)
    
    def tokenize(self):
        for _ in range(self.k):
            pass

corpus = HuggingFaceCorpus()
bpe = BytePairEncoding(corpus.vocabulary, k=3)
dv = bpe.encoding()

#v = set(['t', 'h', 'i', 's', '_', 'f', 'a', 'c', 'w', 'e', 'n', 'v', 'o', 'f', 'b', 'th', 'at', 'the'])
print(dv)