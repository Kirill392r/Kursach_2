import requests

from src.parser import Parser


class HeadHunterAPI(Parser):
    """
    Конкретная реализация VacancyAPI для платформы hh.ru
    """

    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {"User-Agent": "HH-User-Agent"}
        self.params = {"text": "", "page": 0, "per_page": 50}

    def load_vacancies(self, keyword: str) -> list[dict]:
        self.params["text"] = keyword
        self.params["page"] = 0
        all_vacancies = []

        for _ in range(20):
            response = requests.get(self.url, headers=self.headers, params=self.params)
            if response.status_code != 200:
                break
            data = response.json().get("items", [])
            all_vacancies.extend(data)
            self.params["page"] += 1
        return all_vacancies
