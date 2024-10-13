# config.py

# Database Configuration
DB_CONNECTION_STRING = "postgresql://user:password@localhost/dbname"

# LLM Configurations
TECH_CONFIG = {
    "temperature": 0.7,
    "max_tokens": 1000,
}

NONTECH_CONFIG = {
    "temperature": 0.5,
    "max_tokens": 800,
}

# API Configuration
MAX_EXTERNAL_INFO_LENGTH = 5000

# Prompts
TECHNICAL_PROMPT = """You are a technical assistant tasked with providing relevant information about META's Ads for Business, including pricing, usage statistics and configuration specifications. 
Answer the following question using the provided context. 
If the context doesn't contain relevant information, use your general knowledge to answer.

Context: {context}

Question: {question}

Answer:"""

NON_TECHNICAL_PROMPT = """You are a friendly assistant tasked with providing relevant information about META's Ads for Business including usage cases and examples. 
Answer the following question using the provided context. 
If the context doesn't contain relevant information, use your general knowledge to answer in a conversational tone.

Context: {context}

Question: {question}

Answer:"""

SUMMARY_PROMPT = """Summarize the following text, capturing the main points and key details:

{text}

Summary:"""