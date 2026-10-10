from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import END, MessageGraph, StateGraph
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from typing import List, Sequence
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

load_dotenv()   # reads .env and loads GROQ_API_KEY

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0,
)
