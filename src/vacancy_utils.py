from src.vacancy import Vacancy


def filter_vacancies(vacancies: list[Vacancy], keywords: list[str]) -> list[Vacancy]:
    """
    Фильтровать вакансии по ключевым словам в описании.

    :param vacancies: Список вакансий.
    :param keywords: Список ключевых слов.
    :return: Отфильтрованный список вакансий.
    """
    return [
        v
        for v in vacancies
        if any(k.lower() in v.description.lower() for k in keywords)
    ]


def get_vacancies_by_salary(
    vacancies: list[Vacancy], salary_range: str
) -> list[Vacancy]:
    """
    Фильтрация вакансий по диапазону зарплат.

    :param vacancies: Список вакансий.
    :param salary_range: Диапазон зарплат в формате 'min-max'.
    :return: Список вакансий в пределах указанного диапазона зарплат.
    """
    try:
        low, high = map(int, salary_range.split("-"))
        return [v for v in vacancies if low <= v.salary <= high]
    except ValueError:
        return []


def sort_vacancies(vacancies: list[Vacancy]) -> list[Vacancy]:
    """
    Сортировка вакансий по зарплате (по убыванию).

    :param vacancies: Список вакансий.
    :return: Отсортированный список вакансий.
    """
    return sorted(vacancies, reverse=True)


def get_top_vacancies(vacancies: list[Vacancy], top_n: int) -> list[Vacancy]:
    """
    Получить топ N вакансий по зарплате.

    :param vacancies: Список вакансий.
    :param top_n: Количество вакансий в топе.
    :return: Топ N вакансий.
    """
    return vacancies[:top_n]


def print_vacancies(vacancies: list[Vacancy]):
    """
    Вывести вакансии в консоль.

    :param vacancies: Список вакансий.
    """
    for v in vacancies:
        print(v, end="\n\n")
