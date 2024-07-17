from pydantic import Field
from OBDBManager.other.BreweryListBaseTool import BreweryListBaseTool


class GetBreweryNamesTool(BreweryListBaseTool):
    """
    GetBreweryNamesTool is designed to return all brewery names from the list of breweries.
    """

    def run(self):
        return [self.get_name(map_element) for map_element in self.get_brewery_list()]


if __name__ == "__main__":
    tool = GetBreweryNamesTool()
    tool.add_brewery_to_list("Brewery1", "City1", "http://brewery1.com")
    tool.add_brewery_to_list("Brewery2", "City2", "http://brewery2.com")
    print(tool.run())
