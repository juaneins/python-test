import unittest
from unittest.mock import patch
from src.api_client import get_location


class ApiClientTests(unittest.TestCase):

    @patch("src.api_client.requests.get")
    def test_get_location_returns_expected_data(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "countryName": "United States of America",
            "countryCode": "US",
            "regionName": "California",
        }
        result = get_location("8.8.8.8")
        self.assertEqual(
            result.get("country"),
            "United States of America"
        )
