import logging
import pathlib
from src.swapi import SWAPI
from src.top_character_processor import TopCharacterProcessor
from src.csv_utils import build_csv, send_csv_file


def main():
    logging.basicConfig(level=logging.ERROR)
    csv_filepath = f"{pathlib.Path(__file__).parent.absolute()}/output/star_wars_heights.csv"
    http_bin_endpoint = "https://httpbin.org/post"
    swapi = SWAPI(base_url="https://swapi.dev/api")
    etl = TopCharacterProcessor(swapi=swapi, top_character_limit=10)

    top_ten = etl.get_top_characters(sort_by="height")
    build_csv(data=top_ten, fieldnames=['name', 'species', 'height', 'appearances'],
              filepath=csv_filepath)
    send_csv_file(endpoint=http_bin_endpoint, filepath=csv_filepath)


if __name__ == "__main__":
    main()
