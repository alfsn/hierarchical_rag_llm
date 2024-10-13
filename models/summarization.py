from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain

class HierarchicalSummarizer:
    def __init__(self, llm=None):
        self.llm = llm
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

    def summarize(self, document):
        texts = self.text_splitter.split_text(document)
        
        if len(texts) == 1:
            return texts[0]
        
        chain = load_summarize_chain(self.llm, chain_type="map_reduce")
        summary = chain.run(texts)
        
        return summary