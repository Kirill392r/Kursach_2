from src.hh import HeadHunterAPI
from src.json_saver import JSONSaver
from src.vacancy import Vacancy
from src.vacancy_utils import (filter_vacancies, get_top_vacancies,
                               get_vacancies_by_salary, print_vacancies,
                               sort_vacancies)


def user_interaction():
    """
    Функция для взаимодействия с пользователем: поиск вакансий, фильтрация, вывод топ N.
    """
    api = HeadHunterAPI()
    saver = JSONSaver("data/vacancies.json")

    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество топ вакансий: "))
    keywords = input("Введите ключевые слова через пробел: ").split()
    salary_range = input("Введите диапазон зарплат (например: 100000-200000): ")

    raw_data = api.get_vacancies(search_query)
    vacancies = Vacancy.cast_to_object_list(raw_data)

    filtered = filter_vacancies(vacancies, keywords)
    ranged = get_vacancies_by_salary(filtered, salary_range)
    sorted_vacs = sort_vacancies(ranged)
    top_vacs = get_top_vacancies(sorted_vacs, top_n)

    for v in top_vacs:
        saver.add_vacancy(v)

    print_vacancies(top_vacs)
