import logging
from src.exceptions import TopTenCharacterException, FailedFetchingResource


class TopCharacterProcessor:
    """
    TopCharacterProcessor Class transforms Star Wars API data into lists of the
    top star wars characters
    """

    def __init__(self, swapi, top_character_limit=10):
        """
        Constructs TopCharacterProcessor
        :param swapi: Instance of SWAPI (star wars api handler)
        :param top_character_limit: number of characters that should be considered
        """
        self.__top_character_limit = top_character_limit
        self.__swapi = swapi

    def get_top_characters(self, sort_by="appearances") -> list:
        """
        Returns the Top  star wars characters by number of film appearances
        :param sort_by: field to sort results by. OPTIONS: [ "appearances", "height" ] default is
            "appearances"
        :return: List of dictionaries with details of the top ten characters
        """
        try:
            films = self.__swapi.get_all("films")
            appearances_dict = self.__generate_character_appearances_dict(films)
            top_characters, runners_up = self.__filter_top_appearances(appearances_dict)
            top_characters = self.__appearances_tiebreaker(top_characters, runners_up)
            results = self.__construct_response_data(top_characters)
            return self.__sort_results(results, sort_by)
        except FailedFetchingResource as e:
            raise e
        except Exception as e:
            logging.error(f"Failed to get top characters list: {str(e)}")
            raise TopTenCharacterException(f"Failed to get top characters list: {str(e)}")

    def __generate_character_appearances_dict(self, films) -> dict:
        """
        Generate a dict with character urls as keys and number of film appearances as values
        :param films: list of film jsons from swapi
        :return:
        """
        appearances_counter = {}
        for film in films:
            for character_link in film["characters"]:
                count = appearances_counter.get(character_link, 0)
                appearances_counter.update({character_link: count + 1})
        return self.__sort_appearances_by_count(appearances_counter)

    def __filter_top_appearances(self, appearances_dict: dict) -> (list, list):
        """
        filters the characters by appearance into
        :param appearances_dict:
        :return: two lists of character resource links
        """
        top_appearances_urls = []
        runner_up_urls = []
        min_appearances = None
        for url, appearances in appearances_dict.items():
            if not min_appearances or min_appearances == appearances:
                runner_up_urls.append(url)
            elif appearances < min_appearances and self.__sum_list_length(
                    top_appearances_urls, runner_up_urls) > self.__top_character_limit:
                break
            else:
                top_appearances_urls += runner_up_urls
                runner_up_urls = [url]
            min_appearances = appearances
        return top_appearances_urls, runner_up_urls

    def __appearances_tiebreaker(self, top_characters: list, runners_up: list) -> list:
        """
        Breaks a tie in runner up characters should there be one
        :param top_characters:
        :param runners_up:
        :return:
        """
        if runners_up and len(top_characters) != self.__top_character_limit:
            for url in runners_up:
                if len(top_characters) == self.__top_character_limit:
                    break
                # TODO Add tiebreaker logic here. will return first in list for now.
                top_characters.append(url)
        return top_characters

    def __construct_response_data(self, character_urls: list) -> list:
        """
        Builds the results character data
        :param character_urls: list of swapi api urls linking to character resources
        :return: List of dictionaries containing Character information
        """
        result_list = []
        people = self.__swapi.get_resources(character_urls)
        for person in people:
            species = self.__swapi.get_resources(person["species"])
            species = "" if not species else species[0].get("name", "")
            result_list.append(
                {"name": person.get("name", ""), "species": species,
                 "height": person.get("height", "0"),
                 "appearances": len(person.get("films", []))})
        return result_list

    @staticmethod
    def __sort_results(results: list, sort_by: str) -> list:
        """
        Sorts the results by the sort by value
        :param results: list of dicts containing top character results
        :param sort_by: what to sort by Options: ["appearances", "height"]
        :return:
        """
        sort_by = "appearances" if sort_by not in ["appearances", "height"] else sort_by
        return sorted(results, key=lambda k: int(k[sort_by]), reverse=True)

    @staticmethod
    def __sort_appearances_by_count(data: dict) -> dict:
        """
        Sorts appearances dict by count. Most appearances will be at top of the list.
        :param data:
        :return:
        """
        return {k: v for k, v in sorted(data.items(), reverse=True, key=lambda item: item[1])}

    @staticmethod
    def __sum_list_length(list_one: list, list_two: list) -> int:
        """
        Returns the sum of the length of two lists
        :param list_one:
        :param list_two:
        :return:
        """
        return len(list_one) + len(list_two)
