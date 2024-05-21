class Vocabulary:
    def __init__(self, sentences):
        self._init_vocabulary(sentences=sentences)

    def _init_vocabulary(self, sentences):
        splitted_sentences = [
            sentence.split(' ') for sentence in sentences
        ]

        self.vocabulary = []

        for sentence in splitted_sentences:
            for word_i in range(len(sentence)):
                pref = '_' if word_i > 0 else ''
                word = sentence[word_i]
                voc = f"{pref}{word.replace('.', '').replace(',', '').lower()}"
                self.vocabulary.append(voc)
    
    def transform(self):
        return self.vocabulary

class BytePairEncodingVocabulary(Vocabulary):
    def __init__(self, sentences):
        super().__init__(sentences=sentences)
    
    def transform(self):
        voc = []

        for word in self.vocabulary:
            for letter in word:
                voc.append(letter)
        
        return voc
