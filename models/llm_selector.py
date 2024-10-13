import os
from dotenv import load_dotenv
from langchain.llms import Mixtral, LLaMA
from langchain import PromptTemplate, LLMChain
import config

load_dotenv()

api_token = os.environ.get("HUGGINGFACEHUB_API_TOKEN")

class LLMSelector:
    def __init__(self, mixtral_config={}, llama_config={}):
        self.mixtral = Mixtral(**mixtral_config)
        self.llama = LLaMA(**llama_config)
        self.technical_chain = LLMChain(
            llm=self.mixtral,
            prompt=PromptTemplate(template=config.TECHNICAL_PROMPT, input_variables=["context", "question"])
        )
        self.non_technical_chain = LLMChain(
            llm=self.llama,
            prompt=PromptTemplate(template=config.NON_TECHNICAL_PROMPT, input_variables=["context", "question"])
        )

    def select_llm(self, category):
        if category == 'technical':
            return self.technical_chain
        else:
            return self.non_technical_chain