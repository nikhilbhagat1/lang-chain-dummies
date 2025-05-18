from langchain_community.tools.tavily_search import TavilySearchResults


def get_profile_url_tavily(name:str) -> str:
    """ Search for LinkedIn Profile page. """
    search = TavilySearchResults()
    res =  search.run(f"{name} Twitter profile page")
    return res