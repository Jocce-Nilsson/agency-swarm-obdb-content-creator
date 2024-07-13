from agency_swarm import BaseTool
from pydantic import Field
from urllib.request import urlopen
from bs4 import BeautifulSoup

visit_log: list[str] = []


class ExtractLinksTool(BaseTool):
    """
    ExtractLinksTool is designed to extract all the links from a web page.
    It takes a URL as input and returns the links of the web page.
    """
    url: str = Field(
        None, description="The URL of the web page to scrape."
    )

    def run(self, **kwargs):
        if not self.url:
            raise ValueError("URL is required for ExtractLinksTool.")
        if self.url in visit_log:
            raise ValueError("URL has already been visited.")
        visit_log.append(self.url)
        html_page = urlopen(self.url)
        html_text = html_page.read().decode("utf-8")
        soup = BeautifulSoup(html_text, "html.parser")
        # Extract all the links from the web page and return them as a list
        base_url = "/".join(self.url.split("/")[:3])
        result = []
        for link in soup.find_all("a"):
            if link["href"] is not None:
                if link["href"].startswith("http"):
                    result.append(link["href"])
                elif link["href"].startswith("/"):
                    result.append(base_url + link["href"])
        return result


if __name__ == "__main__":
    tool = ExtractLinksTool(url="https://en.wikipedia.org/wiki/Web_scraping")
    print(tool.run())
