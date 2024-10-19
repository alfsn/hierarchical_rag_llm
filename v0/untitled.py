# -*- coding: utf-8 -*-
"""Untitled

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1k8N29vT0aEWh7dzSryz0hy5umLPYBg9t
"""

!python -m pip install -r requirements.txt

"""# Nueva sección"""

import os
from dotenv import load_dotenv
from langchain.llms import HuggingFaceHub
from langchain import PromptTemplate, LLMChain

load_dotenv()

question = 'How to write Hello World in Python?'

api_token = os.environ.get("HUGGINGFACEHUB_API_TOKEN")

# Correcting the repo_id if "Meta-Llama-3-8B" is a valid model
llm = HuggingFaceHub(repo_id="google/flan-t5-small",
                     model_kwargs={
                         "temperature": 0.7
                     },
                     huggingfacehub_api_token=api_token)

# PromptTemplate should come before llm in LLMChain
prompt = PromptTemplate(
    template="""You are a technical assistant tasked with providing relevant information.
                Answer the following question using the provided context.
                If the context doesn't contain relevant information, use your general knowledge to answer.
                Question: {question}
                Answer:""",
    input_variables=["question"]
)

chain = LLMChain(llm=llm, prompt=prompt)

# Pass the question as a dictionary
answer = chain.run({"question": question})

print(answer)