from unittest.mock import MagicMock, patch
from django.test import TestCase
import requests
import json


class SetUpMocks:
    """Construct mocks for tests."""

    def __init__(self):
        """Initialize mocks."""
        self.fake_response = MagicMock()
        self.fake_response.json.return_value = self.return_fake_json()
        self.fake_get = MagicMock(return_value=self.fake_response)

    def return_fake_json(self):
        """Load a fake response from 'mock_requests.json'."""
        with open("test/test_off/mock_requests.json", "r") as file:
            content = json.load(file)
        return content


class TestRequests(TestCase):

    mocks = SetUpMocks()

    @patch("requests.get", mocks.fake_get)
    def test_mock_request(self):
        """
        Test if mocks works.

        Requests mock should return a response with json which contain
        3 products.
        """
        response = requests.get("off_url&params")
        data = response.json()
        self.assertIn("products", data)
        self.assertEqual(len(data["products"]), 3)

    def test_parser(self):
        pass
