import csv

from src.parser import VacancyStorage
from src.vacancy import Vacancy


class CSVSaver(VacancyStorage):
    """Сохраняет данные в CSV файл"""

    def __init__(self, path: str = "data/vacancies.csv"):
        self.path = path

    def add_vacancy(self, vacancy: Vacancy) -> None:
        with open(self.path, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(
                [vacancy.title, vacancy.url, vacancy.salary, vacancy.description]
            )

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        rows = self.load()
        rows = [v for v in rows if v.title != vacancy.title or v.url != vacancy.url]
        with open(self.path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            for v in rows:
                writer.writerow([v.title, v.url, v.salary, v.description])

    def load(self) -> list[Vacancy]:
        vacancies = []
        try:
            with open(self.path, newline="", encoding="utf-8") as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) == 4:
                        title, url, salary, description = row
                        vacancies.append(
                            Vacancy(
                                title=title,
                                url=url,
                                salary=int(salary) if salary.isdigit() else 0,
                                description=description,
                            )
                        )
        except FileNotFoundError:
            pass
        return vacancies
