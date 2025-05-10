import requests
from requests.exceptions import RequestException

from src.parser import Parser


class HeadHunterAPI(Parser):
    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 50}

    def __handle_response(self, response: requests.Response) -> list[dict]:
        try:
            response.raise_for_status()
            return response.json().get("items", [])
        except (RequestException, ValueError):
            return []

    def __connect(self, keyword: str) -> list[dict]:
        self.__params["text"] = keyword
        self.__params["page"] = 0
        all_vacancies = []

        for _ in range(5):
            try:
                response = requests.get(
                    self.__url, headers=self.__headers, params=self.__params, timeout=10
                )
                data = self.__handle_response(response)
                if not data:
                    break
                all_vacancies.extend(data)
                self.__params["page"] += 1
            except RequestException:
                break

        return all_vacancies

    def load_vacancies(self, keyword: str) -> list[dict]:
        return self.__connect(keyword)
