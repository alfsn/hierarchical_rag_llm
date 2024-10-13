import os
from dotenv import load_dotenv
from langchain.llms import LLaMA, HuggingFaceHub
from langchain import PromptTemplate, LLMChain
import config

load_dotenv('../../.env')

api_token = os.environ.get("HUGGINGFACEHUB_API_TOKEN")

class LLMSelector:
    def __init__(self, tech_config={}, nontech_config={}):
        self.techllm = HuggingFaceHub(repo_id="bigscience/bloom-560m", model_kwargs=tech_config, huggingfacehub_api_token=api_token)
        self.nontechllm = LLaMA(**nontech_config)
        self.technical_chain = LLMChain(
            llm=self.techllm,
            prompt=PromptTemplate(template=config.TECHNICAL_PROMPT, input_variables=["context", "question"])
        )
        self.non_technical_chain = LLMChain(
            llm=self.nontechllm,
            prompt=PromptTemplate(template=config.NON_TECHNICAL_PROMPT, input_variables=["context", "question"])
        )

    def select_llm(self, category):
        if category == 'technical':
            return self.technical_chain
        else:
            return self.non_technical_chain