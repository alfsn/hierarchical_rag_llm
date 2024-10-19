import os
from dotenv import load_dotenv
from langchain.llms import HuggingFaceHub
from langchain import PromptTemplate, LLMChain

load_dotenv()

question = 'How to write Hello World in Python?'

api_token = os.environ.get("HUGGINGFACEHUB_API_TOKEN")

# Correcting the repo_id if "Meta-Llama-3-8B" is a valid model
llm = HuggingFaceHub(repo_id="meta-llama/Meta-Llama-3-8B", 
                     model_kwargs={
                         "temperature": 0.7,
                         "max_tokens": 1000,
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
