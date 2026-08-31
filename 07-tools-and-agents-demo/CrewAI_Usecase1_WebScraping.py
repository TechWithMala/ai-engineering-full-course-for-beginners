# pip install crewai
# pip install crewai-tools

from crewai_tools import ScrapeWebsiteTool, TXTSearchTool
from crewai import Agent, Task, Crew
import os

# Scrape Wikipedia website by using CrewAI tool ScrapeWebsiteTool
tool = ScrapeWebsiteTool(website_url='https://en.wikipedia.org/wiki/Artificial_intelligence') 

# Extract the text
text = tool.run()
# print(text)

# Store the scraped data into a text file
os.chdir(r"C:\Users\malah\Documents\Data")
with open("ai.txt", "w", encoding="utf-8") as file:
    file.write(text)

# Using CrewAI tool TXTSearchTool and retrieving the specific context we want
tool = TXTSearchTool(txt='ai.txt')
context = tool.run('What is natural language processing?')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ CREATING AGENT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Define an data_analyst agent
data_analyst = Agent(
    role='Educator',
    goal=f'Based on the context provided, answer the question - What is Natural Language Processing? Context - {context}',
    backstory='You are a data expert',
    verbose=True,
    allow_delegation=False,
    tools=[tool]
)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ CREATING TASK ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Define a task for the data_analyst agent
test_task = Task(
    description="Understand the topic and give the correct response",
    tools=[tool],
    agent=data_analyst,
    expected_output='Give a correct response'
)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ CREATING THE CREW ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Define crew
crew = Crew(
    agents=[data_analyst],
    tasks=[test_task]
)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ RUNNING THE CREW ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
output = crew.kickoff()

print(output.raw)