import json
from typing import List

from src.parser import VacancyStorage
from src.vacancy import Vacancy


class JSONSaver(VacancyStorage):
    """
    Реализация VacancyStorage для хранения в JSON-файле.
    """

    def __init__(self, path: str = "data/vacancies.json"):
        self.path = path

    def _load_raw(self) -> List[dict]:
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save_raw(self, data: List[dict]):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def add_vacancy(self, vacancy: Vacancy) -> None:
        data = self._load_raw()
        data.append(vacancy.__dict__)
        self._save_raw(data)

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        data = self._load_raw()
        data = [
            v for v in data if v["title"] != vacancy.title or v["url"] != vacancy.url
        ]
        self._save_raw(data)

    def load(self) -> List[Vacancy]:
        raw = self._load_raw()
        return [Vacancy(**item) for item in raw]
