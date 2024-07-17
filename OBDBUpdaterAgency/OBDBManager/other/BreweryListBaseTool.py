from abc import abstractmethod

from agency_swarm.tools import BaseTool

NAME_KEY = "name"
CITY_KEY = "city"
URL_KEY = "url"
# Define a list to hold the breweries
brewery_list: list[map] = []


class BreweryListBaseTool(BaseTool):
    """
    BreweryListBaseTool is a base class for tools that interact with a list of breweries.
    """

    @abstractmethod
    def run(self, **kwargs):
        pass

    @staticmethod
    def brewery_exists(brewery_name):
        """
        Helper method to check if a brewery with the given name already exists in the list.
        """
        for brewery in brewery_list:
            if brewery[NAME_KEY] == brewery_name:
                return True
        return False

    @staticmethod
    def is_valid_url(url):
        """
        Helper method to check if a URL is in a valid format.
        """
        return url.startswith("http://") or url.startswith("https://")

    @staticmethod
    def add_brewery_to_list(brewery_name, city, url):
        """
        Helper method to add a brewery to the list of breweries.
        """
        brewery_list.append({NAME_KEY: brewery_name, CITY_KEY: city, URL_KEY: url})

    @staticmethod
    def get_brewery_list():
        """
        Static method to get the list of breweries.
        """
        return brewery_list

    @staticmethod
    def is_brewery_list_empty():
        """
        Static method to check if the list of breweries is empty.
        """
        return len(brewery_list) == 0

    @staticmethod
    def pop_brewery_list():
        """
        Static method to get the first map element the list of breweries. The element is removed from the list.
        """
        return brewery_list.pop()

    @staticmethod
    def get_name(map_element):
        """
        Static method to get the name of a brewery from a map element.
        """
        return map_element[NAME_KEY]

    @staticmethod
    def get_city(map_element):
        """
        Static method to get the city of a brewery from a map element.
        """
        return map_element[CITY_KEY]

    @staticmethod
    def get_url(map_element):
        """
        Static method to get the URL of a brewery from a map element.
        """
        return map_element[URL_KEY]
