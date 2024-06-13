# first pip install crewai
from langchain_community.llms import Ollama
from crewai import Agent,Task,Crew,Process

model = Ollama(model="llama3")

# code = "console.log(`hello world`)"

email = "hey your neighbour jhon here , your house seems to be on fire .this is not a joke" #the statement which we want to input

classifier = Agent(
    role = "email classifier",
    goal = "accurately classify emails based on theri importance. give every email one of these ratings:important, casual or spam",
    backstory = "You are an AI assistant whose job is to classify mails",
    verbose = True,
    allow_delegation = False,
    llm = model
)

responder = Agent(
    role = "email responder",
    goal = "respond to emails based on their importance. Respond to important emails first then casual emails, and ignore spam emails",
    backstory = "You are an AI assistant whose job is to respond mails",
    verbose = True,
    allow_delegation = False,
    llm = model
)

classify_email = Task(
    description = f"Classify the following email : '{email}'",
    agent = classifier,
    expected_output = "One of these three options : 'important', 'casual' or 'spam'",
)
respond_to_email = Task(
    description = f"Respond to email : '{email}' based on the importance provided by the '{classifier} agent.", #ya to ye ya to bas cassifier
    agent = classifier,
    expected_output = "A very concise response to email based on importance provided by the '{classifier} agent.",
)
crew = Crew(
    agents= [classifier,responder],
    tasks= [classify_email,respond_to_email],
    verbose=2,
    process=Process.sequential
)
output = crew.kickoff()
print(output)