from src.csv_saver import CSVSaver
from src.hh import HeadHunterAPI
from src.json_saver import JSONSaver
from src.txt_saver import TXTSaver
from src.vacancy import Vacancy
from src.vacancy_utils import (filter_vacancies, get_top_vacancies,
                               get_vacancies_by_salary, print_vacancies,
                               sort_vacancies)


def get_storage_by_format(fmt: str):
    match fmt.lower():
        case "json":
            return JSONSaver()
        case "csv":
            return CSVSaver()
        case "txt":
            return TXTSaver()
        case _:
            raise ValueError(
                "Неподдерживаемый формат файла. Выберите: json, csv, txt, excel."
            )


def main():
    hh_api = HeadHunterAPI()
    search_query = input("Введите поисковый запрос: ")
    hh_vacancies = hh_api.load_vacancies(search_query)

    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат (например, 100000-150000): ")

    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)

    # выбор формата
    file_format = input("Введите формат сохранения (json, csv, txt): ")
    saver = get_storage_by_format(file_format)

    for vacancy in top_vacancies:
        saver.add_vacancy(vacancy)


if __name__ == "__main__":
    main()
