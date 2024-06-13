# first pip install crewai
from langchain_community.llms import Ollama
from crewai import Agent,Task,Crew,Process

model = Ollama(model="llama3:8b")

# code = "console.log(`hello world`)"

email = "nigerian prince sending some gold" #the statement which we want to input

classifier = Agent(
    role="email classifier"
    
)


