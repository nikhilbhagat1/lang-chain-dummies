from dotenv import load_dotenv
from langchain.chains.summarize.map_reduce_prompt import prompt_template
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()
from langchain_community.chat_models import ChatOpenAI, ChatOllama
from langchain.prompts.prompt import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)
from langchain import hub
from tools.tools import get_profile_url_tavily


def lookup(name: str) -> str:
    llm = ChatOllama(model="llama3")
    template = """Given the full name {name_of_person}, return ONLY the URL to their LinkedIn profile page. Do not include any other text, explanation, or formatting. Only output the URL."""
    prompt_template = PromptTemplate(template=template, input_variables=["name_of_person"])
    tools_for_agent = [
        Tool(
            name="Crawl Google for LinkedIn Profile page",
            func=get_profile_url_tavily,
            description="useful for when you need get the LinkedIn Page URL "
        )
    ]
    react_pull = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_pull)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)
    output_parser = JsonOutputParser()
    result = output_parser.invoke(agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}#,"handle_parsing_errors": True}
    ))
    linkedin_profile_url = result["output"]
    print(linkedin_profile_url)
    return linkedin_profile_url  # <-- Add this line to return the URL

#
# if __name__ == '__main__':
#     linkedin_url = lookup(name="Eden Marco")
#     print(linkedin_url)
