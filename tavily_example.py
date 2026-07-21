import os
from dotenv import load_dotenv
from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent 




load_dotenv()

os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")

def search (query:str) -> str:
    print(f"Searching for: {query}")

    return f"Search results for: {query}"

def main():
    print("Hello from langchain-course!")
    llm = ChatOpenAI()
    tools = [search]

