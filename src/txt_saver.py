from src.parser import VacancyStorage
from src.vacancy import Vacancy


class TXTSaver(VacancyStorage):
    """Сохраняет данные в TXT файл"""

    def __init__(self, path: str = "data/vacancies.txt"):
        self.path = path

    def add_vacancy(self, vacancy: Vacancy) -> None:
        with open(self.path, "a", encoding="utf-8") as f:
            f.write(
                f"{vacancy.title}||{vacancy.url}||{vacancy.salary}||{vacancy.description}\n"
            )

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        lines = []
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except FileNotFoundError:
            pass

        with open(self.path, "w", encoding="utf-8") as f:
            for line in lines:
                parts = line.strip().split("||")
                if len(parts) == 4 and (
                    parts[0] != vacancy.title or parts[1] != vacancy.url
                ):
                    f.write(line)

    def load(self) -> list[Vacancy]:
        vacancies = []
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                for line in f:
                    parts = line.strip().split("||")
                    if len(parts) == 4:
                        title, url, salary, description = parts
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
