import numpy as np
from utils.database import FAQDatabase # custom FAQ database
from utils.vector_operations import cosine_similarity

class QuestionCategorizer:
    def __init__(self, faq_db: FAQDatabase, threshold=0.8):
        self.faq_db = faq_db
        self.threshold = threshold

    def categorize(self, question_embedding):
        faqs = self.faq_db.get_all_faqs()
        similarities = [cosine_similarity(question_embedding, faq.embedding) for faq in faqs]
        max_similarity = max(similarities)
        
        if max_similarity > self.threshold:
            return faqs[np.argmax(similarities)].category
        else:
            return 'unknown'
            # not sure if this should return text or not