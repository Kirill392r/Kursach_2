from typing import Optional


class Vacancy:
    """
    Класс для представления вакансии с аттрибутами и методами.
    """

    def __init__(self, title: str, url: str, salary: Optional[int], description: str):
        """
        Инициализация объекта вакансии.

        :param title: Название вакансии.
        :param url: Ссылка на вакансию.
        :param salary: Зарплата (может быть None, если не указана).
        :param description: Описание вакансии.
        """
        self.title = title
        self.url = url
        self.salary = self._parse_salary(salary)
        self.description = description

    @staticmethod
    def _parse_salary(salary: Optional[int]) -> int:
        """
        Преобразование зарплаты в целое число. Если зарплата не указана, возвращает 0.

        :param salary: Зарплата.
        :return: Зарплата как целое число.
        """
        if isinstance(salary, int):
            return salary
        if isinstance(salary, str) and salary.strip().isdigit():
            return int(salary.strip())
        return 0

    def __str__(self) -> str:
        """
        Строковое представление вакансии.

        :return: Строка с названием, зарплатой, ссылкой и описанием вакансии.
        """
        return f"{self.title} ({self.salary} руб.): {self.url}\n{self.description}"

    def __lt__(self, other: "Vacancy") -> bool:
        """
        Сравнение вакансий по зарплате.

        :param other: Другая вакансия.
        :return: True, если зарплата текущей вакансии меньше, чем у другой.
        """
        return self.salary < other.salary

    def __eq__(self, other: "Vacancy") -> bool:
        """
        Проверка равенства вакансий по зарплате.

        :param other: Другая вакансия.
        :return: True, если зарплаты равны.
        """
        return self.salary == other.salary

    @classmethod
    def cast_to_object_list(cls, data_list: list[dict]) -> list["Vacancy"]:
        """
        Преобразование списка вакансий из формата JSON в список объектов Vacancy.

        :param data_list: Список вакансий в формате JSON.
        :return: Список объектов Vacancy.
        """
        vacancies = []
        for item in data_list:
            salary = item.get("salary", {})
            salary_from = salary.get("from") if salary else 0
            v = cls(
                title=item.get("name"),
                url=item.get("alternate_url"),
                salary=salary_from,
                description=item.get("snippet", {}).get("requirement", "")
                or "Нет описания",
            )
            vacancies.append(v)
        return vacancies
