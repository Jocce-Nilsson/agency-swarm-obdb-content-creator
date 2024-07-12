from agency_swarm import BaseTool
from pydantic import Field
from urllib.request import urlopen
from bs4 import BeautifulSoup


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
        html_page = urlopen(self.url)
        html_text = html_page.read().decode("utf-8")
        soup = BeautifulSoup(html_text, "html.parser")
        return soup.get_text().strip()


if __name__ == "__main__":
    tool = ScrapingTool(url="https://en.wikipedia.org/wiki/Web_scraping")
    print(tool.run())
