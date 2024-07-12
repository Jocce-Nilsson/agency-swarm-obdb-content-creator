from agency_swarm.tools import BaseTool
from pydantic import Field
from googleapiclient.discovery import build
import os
import pprint


class GoogleSearchTool(BaseTool):
    """
    GoogleSearchTool is designed to search the web using the Google Custom Search API and a dedicated search engine.
    It takes a query string as input and returns the search results in form of a list of dict objects with keys
    title, link and snippet.
    """

    key: str = Field(
        os.getenv("GOOGLE_SEARCH_API_KEY"), description="The Google Search API key. Default is taken from environment "
                                                        "variable GOOGLE_SEARCH_API_KEY."
    )
    cx: str = Field(
        os.getenv("GOOGLE_SEARCH_ENGINE_ID"), description="The Google Search Engine ID. Default is taken from "
                                                          "environment variable GOOGLE_SEARCH_ENGINE_ID."
    )
    query: str = Field(
        None, description="The query string to search for on the web."
    )

    def validate_required_environment_variables(self):
        if not self.key:
            # Google Search API key is required, throw an error if not provided
            raise ValueError("Google Search API key is required for GoogleSearchTool.")
        if not self.cx:
            # Google Search Engine ID is required, throw an error if not provided
            raise ValueError("Google Search Engine ID is required for GoogleSearchTool.")

    def run(self):
        self.validate_required_environment_variables()
        if not self.query:
            # Query is required for GoogleSearchTool, throw an error if not provided
            raise ValueError("Query is required for GoogleSearchTool.")
        service = build("customsearch", "v1", developerKey=self.key)
        res = (service.cse().list(q=self.query, cx=self.cx, num=10, start=1).execute())
        result_list = [{'title': item['title'], 'link': item['link'], 'snippet': item['snippet']} for item in res['items']]
        res = (service.cse().list(q=self.query, cx=self.cx, num=10, start=11).execute())
        result_list += [{'title': item['title'], 'link': item['link'], 'snippet': item['snippet']} for item in res['items']]
        res = (service.cse().list(q=self.query, cx=self.cx, num=10, start=21).execute())
        result_list += [{'title': item['title'], 'link': item['link'], 'snippet': item['snippet']} for item in res['items']]
        res = (service.cse().list(q=self.query, cx=self.cx, num=10, start=31).execute())
        result_list += [{'title': item['title'], 'link': item['link'], 'snippet': item['snippet']} for item in res['items']]
        return result_list


if __name__ == "__main__":
    tool = GoogleSearchTool(query="Python programming")
    pprint.pprint(tool.run())
