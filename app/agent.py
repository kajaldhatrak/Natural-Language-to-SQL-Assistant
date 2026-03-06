import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

from langchain_openai import ChatOpenAI
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent

load_dotenv()

DB_URI = os.getenv("DB_URI")

engine = create_engine(DB_URI)

db = SQLDatabase(engine)

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

agent_executor = create_sql_agent(
    llm=llm,
    db=db,
    agent_type="openai-tools",
    verbose=True
)

def ask_database(question: str):
    response = agent_executor.invoke({"input": question})
    return response["output"]