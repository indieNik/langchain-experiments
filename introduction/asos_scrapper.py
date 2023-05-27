from dotenv import find_dotenv, load_dotenv
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.agents.load_tools import get_all_tool_names
from langchain import ConversationChain

# Load environment variables
load_dotenv(find_dotenv())


llm = OpenAI(temperature=0)

toolNames = get_all_tool_names()
tools = load_tools(["python_repl"], llm=llm)

# Finally, let's initialize an agent with the tools, the language model, and the type of agent we want to use.
agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

# Now let's test it out!
result = agent.run("""
Analyse the page 'https://www.asos.com/men/summer-essentials/cat/?cid=50085' using selenium (import By & webdriver).
Save all the product data to a CSV file named 'asos_listings.csv'
Here are the locators:
titles = driver.find_elements(By.CSS_SELECTOR, 'article a div p')
prices = driver.find_elements(By.CSS_SELECTOR, 'article a > p')
images = driver.find_elements(By.CSS_SELECTOR, 'article a img')
Load more until you 
""")
print(result)
