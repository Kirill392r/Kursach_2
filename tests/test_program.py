from src.vacancy import Vacancy


def test_vacancy_comparison():
    v1 = Vacancy("Test", "url", 100000, "desc")
    v2 = Vacancy("Test2", "url2", 150000, "desc")
    assert v1 < v2


def test_salary_parse_string():
    v = Vacancy("Test", "url", "100000", "desc")
    assert v.salary == 100000


def test_salary_fallback():
    v = Vacancy("Test", "url", None, "desc")
    assert v.salary == 0


def test_vacancy_comparison_lt_eq():
    v1 = Vacancy("Python Dev", "url1", 100000, "desc")
    v2 = Vacancy("Senior Dev", "url2", 150000, "desc")
    v3 = Vacancy("Middle Dev", "url3", 100000, "desc")

    assert v1 < v2
    assert not v2 < v1
    assert v1 == v3
    assert v1 != v2


def test_cast_to_object_list():
    data = [
        {
            "name": "Backend Developer",
            "alternate_url": "https://hh.ru/vacancy/123",
            "salary": {"from": 120000},
            "snippet": {"requirement": "Опыт от 3 лет"},
        },
        {
            "name": "Junior Dev",
            "alternate_url": "https://hh.ru/vacancy/456",
            "salary": None,
            "snippet": {},
        },
    ]

    vacancies = Vacancy.cast_to_object_list(data)

    assert len(vacancies) == 2
    assert vacancies[0].title == "Backend Developer"
    assert vacancies[0].salary == 120000
    assert vacancies[1].salary == 0
    assert vacancies[1].description == "Нет описания"
