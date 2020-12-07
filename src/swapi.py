import requests
import logging
from src.exceptions import FailedFetchingResource


class SWAPI:

    def __init__(self, base_url: str):
        self.__base_url = base_url

    def get_all(self, resource: str) -> list:
        """
        Returns all results for the provided resource
        :param resource:
        :return:
        """
        endpoint = f"{self.__base_url}/{resource}"
        results = []
        next_page = True
        while next_page:
            json_response = self.__call_api(endpoint)
            results += json_response.get("results", [])
            next_page = json_response.get("next")
        return results

    def get_resources(self, url_list: list) -> list:
        """
        Given a list of Star Wars API resources will return a list each resources data
        :param url_list: list of resource urls
        :return:
        """
        resource_list = []
        for url in url_list:
            resource_list.append(self.__call_api(url))
        return resource_list

    @staticmethod
    def __call_api(endpoint: str) -> dict:
        """
        Returns the Json data in Dict form when provided the full endpoint.
        :param endpoint:
        :return:
        """
        try:
            response = requests.get(endpoint, timeout=15)
            if response.status_code != 200:
                raise FailedFetchingResource()
            return response.json()
        except Exception as e:
            logging.error(f"GET request to SWAPI failed to retrieve resource: {str(e)}")
            raise FailedFetchingResource(
                f"GET request to SWAPI failed to retrieve resource: {str(e)}")
