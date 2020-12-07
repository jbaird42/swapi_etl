import logging
import os
import pathlib
from src.swapi import SWAPI
from src.top_character_processor import TopCharacterProcessor
from src.csv_utils import build_csv, send_csv_file


def main():
    logging.basicConfig(level=logging.ERROR)
    csv_filepath = f"{pathlib.Path(__file__).parent.absolute()}/output/star_wars_heights.csv"
    swapi = SWAPI(base_url="https://swapi.dev/api")
    etl = TopCharacterProcessor(swapi=swapi,
                                top_character_limit=int(os.getenv("TOP_SW_CHARACTER_LIMIT", 10)))
    top_ten = etl.get_top_characters(sort_by="height")
    build_csv(data=top_ten, fieldnames=['name', 'species', 'height', 'appearances'],
              filepath=csv_filepath)
    response = send_csv_file(endpoint="https://httpbin.org/post",
                             filepath=csv_filepath)
    print(f"Successfully Pushed CSV:\n{response['files'].get('file')}")


if __name__ == "__main__":
    main()
