from vocabulary import Vocabulary, BytePairEncodingVocabulary

class Corpus:
    def __init__(self, sentences):
        self.sentences = sentences
        self.vocabulary = BytePairEncodingVocabulary(
            sentences=self.sentences
        ).transform()

class HuggingFaceCorpus(Corpus):
    def __init__(self):
        super().__init__(sentences=[
            "This is the Hugging Face Course.",
            "This chapter is about tokenization.",
            "This section shows several tokenizer algorithms.",
            "Hopefully, you will be able to understand how they are trained and generate tokens.",
        ])

class SlideExampleCorpus(Corpus):
    def __init__(self):
        super().__init__(
            sentences=['This fat cat with the hat is in the cave of the thin bat']
        )