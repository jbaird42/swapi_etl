import unittest
import os
import pathlib
import csv
import requests_mock
from src.exceptions import  FailedPOST, FailedBuildingCSV
from src.csv_utils import build_csv, send_csv_file


class TestCsvUtils(unittest.TestCase):

    @requests_mock.Mocker()
    def test_send_csv_file(self, m):
        test_endpoint = "https://www.test.com"
        m.post(test_endpoint, json={"test": "test"})
        path = pathlib.Path(__file__).parent.absolute()
        response = send_csv_file(test_endpoint, f"{path}/dummy.csv")
        self.assertEqual(response["test"], "test")

    @requests_mock.Mocker()
    def test_send_csv_file_failure(self, m):
        test_endpoint = "https://www.test.com"
        m.post(test_endpoint, status_code=500)
        with self.assertRaises(FailedPOST):
            path = pathlib.Path(__file__).parent.absolute()
            response = send_csv_file(test_endpoint, f"{path}/dummy.csv")

    def test_build_csv(self):
        test_file = "test.csv"
        build_csv(data=[{"test": "test", "status": "success"}], fieldnames=["test", "status"],
                  filepath=test_file)
        with open(test_file, 'r') as my_file:
            reader = csv.DictReader(my_file)
            row = next(reader)
            self.assertEqual(row["status"], "success")
        os.remove(test_file)

    def test_build_csv_failure(self):
        test_file = "test.csv"
        with self.assertRaises(FailedBuildingCSV):
            build_csv(data=["garbage"], fieldnames=[1],
                      filepath=test_file)
        os.remove(test_file)