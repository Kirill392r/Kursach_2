from src.vacancy import Vacancy
from src.vacancy_utils import (filter_vacancies, get_top_vacancies,
                               get_vacancies_by_salary, print_vacancies)


def test_filter_vacancies(sample_vacancies):
    sample_vacancies.append(
        Vacancy(
            "Python Developer with Data Science",
            "http://example.com/4",
            100000,
            "Python, data, and machine learning",
        )
    )

    keywords = ["python", "data"]
    result = filter_vacancies(sample_vacancies, keywords)
    assert len(result) == 2
    assert sample_vacancies[2] in result
    assert sample_vacancies[3] in result


def test_get_top_vacancies(sample_vacancies):
    sorted_vacancies = sorted(sample_vacancies, key=lambda v: v.salary, reverse=True)
    top_vacancies = get_top_vacancies(sorted_vacancies, 2)

    assert len(top_vacancies) == 2
    assert sorted_vacancies[0] in top_vacancies
    assert sorted_vacancies[1] in top_vacancies
    assert sorted_vacancies[2] not in top_vacancies


def test_print_vacancies(sample_vacancies, capsys):
    print_vacancies(sample_vacancies)
    captured = capsys.readouterr()

    assert "Senior Python Developer" in captured.out
    assert "Junior Python Developer" in captured.out
    assert "Python Developer with Data Analysis" in captured.out


def test_get_vacancies_by_salary_invalid_range(sample_vacancies):
    salary_range = "invalid-range"
    result = get_vacancies_by_salary(sample_vacancies, salary_range)

    assert result == []
