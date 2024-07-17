from pydantic import Field
from OBDBManager.other.BreweryListBaseTool import BreweryListBaseTool


class GetBreweryFromListTool(BreweryListBaseTool):
    """
    GetBreweryFromListTool is designed to get the first brewery from the list of breweries for iteration.
    The tool will remove the brewery from the list and return the name, city and URL of the brewery.
    """

    def run(self):
        if not self.get_brewery_list():
            return "No more breweries in the list."
        map_element = self.pop_brewery_list()
        return (f"Name: {self.get_name(map_element)}\n"
                f"City: {self.get_city(map_element)}\n"
                f"URL: {self.get_url(map_element)}")


if __name__ == "__main__":
    tool = GetBreweryFromListTool()
    tool.add_brewery_to_list("Brewery1", "City1", "http://brewery1.com")
    tool.add_brewery_to_list("Brewery2", "City2", "http://brewery2.com")
    print(tool.run())
    print(tool.run())