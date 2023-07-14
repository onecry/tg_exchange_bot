import requests
from typing import Dict, Any
from config_data.config import RAPID_API_KEY, RAPID_API_HOST


def response() -> str:
	url = "https://currency-exchange.p.rapidapi.com/listquotes"

	headers = {
		"X-RapidAPI-Key": RAPID_API_KEY,
		"X-RapidAPI-Host": RAPID_API_HOST
	}

	response = requests.request("GET", url, headers=headers, timeout=10)

	if response.status_code == requests.codes.ok:

		return response.json()

list_of_currencies: str = response()


def get_exchanged_value(querystring: Dict) -> str:
	url = "https://currency-exchange.p.rapidapi.com/exchange"

	headers = {
		"X-RapidAPI-Key": RAPID_API_KEY,
		"X-RapidAPI-Host": RAPID_API_HOST
	}

	response = requests.request("GET", url, headers=headers, params=querystring, timeout=10)

	if response.status_code == requests.codes.ok:

		exchanged_value = response.json()

		return exchanged_value
