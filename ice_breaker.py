from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
##from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOpenAI, ChatOllama
from langchain_core.output_parsers import StrOutputParser

from agents.linkedin_lookup_agents import lookup
from third_parties.linkedin import scrape_linkedin_profile



def ice_breaker() -> str:
    summary_template = """
    Act as Hiring Manager,  Given information {information} about a person a linkedin
    1. review the profile
    2. write a short summary
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOllama(model="llama3")
    #llm = ChatOllama(model="mistral")

    chain = summary_prompt_template | llm | StrOutputParser()
    linkedin_information = scrape_linkedin_profile("https://www.linkedin.com/in/nikhil~bhagat/", False)
    res = chain.invoke(input={"information": linkedin_information})

    print(res)

def ice_breaker_with(name:str) -> str:

    linkedin_username = lookup(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_username, False)
    summary_template = """
    Given information {information} about a person a Linkedin profile
    1. A short summary
    2. Two interesting facts about the person
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOllama(model="llama3")
    #llm = ChatOllama(model="mistral")

    chain = summary_prompt_template | llm | StrOutputParser()

    res = chain.invoke(input={"information": linkedin_data})

    print(res)

if __name__ == "__main__":
    load_dotenv()

    print("Hello LangChain")
    ice_breaker_with(name="Eden Marco")

