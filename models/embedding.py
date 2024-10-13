from sentence_transformers import SentenceTransformer

class EmbeddingGenerator:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)

    def generate(self, text):
        # encodes the input user query text into the embedding using the selected transformer
        return self.model.encode(text)