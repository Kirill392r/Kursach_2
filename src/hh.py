import requests
from requests.exceptions import RequestException

from src.parser import Parser


class HeadHunterAPI(Parser):
    """
    Конкретная реализация VacancyAPI для платформы hh.ru
    """

    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 50}

    def __connect(self, keyword: str) -> list[dict]:
        """
        Приватный метод для запроса к API hh.ru
        """
        self.__params["text"] = keyword
        self.__params["page"] = 0
        all_vacancies = []

        for _ in range(5):
            try:
                response = requests.get(
                    self.__url, headers=self.__headers, params=self.__params
                )
                response.raise_for_status()
                data = response.json().get("items", [])
                all_vacancies.extend(data)
                self.__params["page"] += 1
            except RequestException:
                return []
            except ValueError:
                return []
        return all_vacancies

    def load_vacancies(self, keyword: str) -> list[dict]:
        """
        Публичный метод
        """
        return self.__connect(keyword)
