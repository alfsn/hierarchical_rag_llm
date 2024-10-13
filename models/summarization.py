from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from langchain import PromptTemplate
import config

class HierarchicalSummarizer:
    def __init__(self, llm):
        self.llm = llm
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        self.summary_prompt = PromptTemplate(template=config.SUMMARY_PROMPT, input_variables=["text"])

    def summarize(self, document):
        texts = self.text_splitter.split_text(document)
        
        if len(texts) == 1:
            return texts[0]
        
        chain = load_summarize_chain(self.llm, chain_type="map_reduce", map_prompt=self.summary_prompt, combine_prompt=self.summary_prompt)
        summary = chain.run(texts)
        
        return summary