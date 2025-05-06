from abc import ABC, abstractmethod

from src.vacancy import Vacancy


class Parser(ABC):
    """
    Абстрактный базовый класс для API-парсеров вакансий.
    """

    @abstractmethod
    def  load_vacancies(self, keyword: str) -> list[dict]:
        """
        Метод для получения вакансий по ключевому слову.
        :param keyword: Ключевое слово для поиска.
        """
        pass


class VacancyStorage(ABC):
    """
    Абстрактный базовый класс для работы с хранилищами вакансий.
    """

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        """
        Добавление вакансии в хранилище.
        """
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """
        Удаление вакансии из хранилища.
        """
        pass

    @abstractmethod
    def load(self) -> list[Vacancy]:
        """
        Загрузка вакансий из хранилища.
        """
        pass
