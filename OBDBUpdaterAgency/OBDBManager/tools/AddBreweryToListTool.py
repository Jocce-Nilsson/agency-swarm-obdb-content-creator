from pydantic import Field
from OBDBManager.other.BreweryListBaseTool import BreweryListBaseTool


class AddBreweryToListTool(BreweryListBaseTool):
    """
    AddBreweryToListTool is designed to add a brewery to the list of breweries.
    """

    brewery_name: str = Field(
        ..., description="The name of the brewery."
    )
    city: str = Field(
        ..., description="The city where the brewery is located."
    )
    url: str = Field(
        ..., description="The URL of the brewery to be added to the list."
    )

    def run(self):
        if not self.url:
            raise ValueError("URL is required for AddBreweryToListTool.")
        if not self.brewery_name:
            raise ValueError("Brewery name is required for AddBreweryToListTool.")
        if not self.city:
            raise ValueError("City is required for AddBreweryToListTool.")
        if self.brewery_exists(self.brewery_name):
            raise ValueError("Brewery already exists in the list.")
        if not self.is_valid_url(self.url):
            raise ValueError("Invalid URL format.")
        if self.url.find("ratebeer") != -1:
            raise ValueError("Ratebeer URLs are not allowed.")
        if self.url.find("untappd") != -1:
            raise ValueError("Untappd URLs are not allowed.")
        self.add_brewery_to_list(self.brewery_name, self.city, self.url)
        return f"{self.brewery_name} added to the list."


if __name__ == "__main__":
    tool = AddBreweryToListTool(brewery_name="Brewery1", city="City1", url="http://brewery1.com")
    print(tool.run())
