from flask import Flask, request, jsonify
from models.embedding import EmbeddingGenerator
from models.categorization import QuestionCategorizer
from models.llm_selector import LLMSelector
from models.summarization import HierarchicalSummarizer
from utils.database import FAQDatabase, ExternalInfoDatabase, QADatabase
from utils.privacy_filter import PrivacyFilter
import config

app = Flask(__name__)

embedding_generator = EmbeddingGenerator()
faq_db = FAQDatabase(config.DB_CONNECTION_STRING)
question_categorizer = QuestionCategorizer(faq_db)
llm_selector = LLMSelector(config.MIXTRAL_CONFIG, config.LLAMA_CONFIG)
external_info_db = ExternalInfoDatabase(config.DB_CONNECTION_STRING)
qa_db = QADatabase(config.DB_CONNECTION_STRING)
privacy_filter = PrivacyFilter()

#  The following function will be associated with the URL /ask. It will trigger the execution of the ask_question function. the route should only handle POST requests.
@app.route('/ask', methods=['POST']) 
def ask_question():
    data = request.json
    question = data['question']
    
    #  embedding using the custom generator
    embedding = embedding_generator.generate(question)
    
    # return technical or non/technical
    category = question_categorizer.categorize(embedding)
    
    llm_chain = llm_selector.select_llm(category)
    
    # Retrieve external info (for RAG)
    external_info = external_info_db.get_relevant_info(embedding)
    if len(external_info) > config.MAX_EXTERNAL_INFO_LENGTH:
        summarizer = HierarchicalSummarizer(llm_chain.llm)
        external_info = summarizer.summarize(external_info)

    answer = llm.generate(question, external_info)
    
    filtered_answer = privacy_filter.filter(answer)
    
    # Store QA pair
    qa_db.store(question, filtered_answer)
    
    return jsonify({'answer': filtered_answer})

if __name__ == '__main__':
    app.run(debug=True)