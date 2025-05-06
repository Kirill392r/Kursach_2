from src.hh import HeadHunterAPI
from src.json_saver import JSONSaver
from src.vacancy import Vacancy
from src.vacancy_utils import (
    filter_vacancies,
    get_top_vacancies,
    get_vacancies_by_salary,
    print_vacancies,
    sort_vacancies,
)


def main():

    hh_api = HeadHunterAPI()
    search_query = input("Введите поисковый запрос: ")
    hh_vacancies = hh_api.get_vacancies(search_query)

    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат (например, 100000-150000): ")

    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)

    json_saver = JSONSaver()
    for vacancy in top_vacancies:
        json_saver.add_vacancy(vacancy)


if __name__ == "__main__":
    main()
