import requests
import logging
import csv
from src.exceptions import FailedPOST, FailedBuildingCSV


def send_csv_file(endpoint: str, filepath: str):
    """
    Send a CSV file via POST
    :param endpoint: url where the csv should be sent
    :param filepath: path to file
    :return:
    """
    try:
        with open(filepath, 'rb') as file:
            files = [
                ('file', ('file', file, 'application/octet-stream'))
            ]
            headers = {
                'Content': 'text/csv'
            }
            response = requests.post(endpoint, headers=headers, files=files)

        if response.status_code != 200:
            raise FailedPOST()
        return response.json()
    except Exception as e:
        logging.error(f"Failed to POST CSV: {str(e)}")
        raise FailedPOST(f"Failed to POST CSV: {str(e)}")


def build_csv(data: list, fieldnames: list, filepath: str):
    try:
        with open(filepath, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for item in data:
                writer.writerow(item)
    except Exception as e:
        logging.error(f"Failed to build CSV: {str(e)}")
        raise FailedBuildingCSV(f"Failed to build CSV: {str(e)}")