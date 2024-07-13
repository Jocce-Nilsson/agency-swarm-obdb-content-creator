import time

from agency_swarm import BaseTool
from pydantic import Field
from urllib.request import urlopen
from bs4 import BeautifulSoup

visit_log: list[str] = []


class ScrapingTool(BaseTool):
    """
    ScrapingTool is designed to scrape web pages using the BeautifulSoup library.
    It takes a URL as input and returns the text content of the web page.
    """
    url: str = Field(
        None, description="The URL of the web page to scrape."
    )

    def run(self, **kwargs):
        if not self.url:
            raise ValueError("URL is required for ScrapingTool.")
        if self.url in visit_log:
            raise ValueError("URL has already been visited.")
        visit_log.append(self.url)
        time.sleep(10)
        html_page = urlopen(self.url)
        html_text = html_page.read().decode("utf-8")
        soup = BeautifulSoup(html_text, "html.parser")
        return soup.get_text().strip()


if __name__ == "__main__":
    tool = ScrapingTool(url="https://en.wikipedia.org/wiki/Web_scraping")
    print(tool.run())
