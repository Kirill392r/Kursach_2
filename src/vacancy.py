from typing import Any, Optional


class Vacancy:
    """
    Класс для представления вакансии с аттрибутами и методами.
    """

    __slots__ = ("title", "url", "salary", "description")

    def __init__(
        self,
        title: Any | None,
        url: Any | None,
        salary: Optional[int],
        description: str,
    ):
        """
        Инициализация объекта вакансии.

        :param title: Название вакансии.
        :param url: Ссылка на вакансию.
        :param salary: Зарплата (может быть None, если не указана).
        :param description: Описание вакансии.
        """
        self.title = title
        self.url = url
        self.salary = self.__parse_salary(salary)
        self.description = description

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "url": self.url,
            "salary": self.salary,
            "description": self.description,
        }

    @staticmethod
    def __parse_salary(salary: Optional[int]) -> int:
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

    def __eq__(self, other: object) -> bool:
        """
        Проверка равенства вакансий по зарплате.

        :param other: Другая вакансия.
        :return: True, если зарплаты равны.
        """
        if not isinstance(other, Vacancy):
            return NotImplemented
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
