import os

from src.csv_saver import CSVSaver
from src.vacancy import Vacancy

TEST_CSV_PATH = "tests/test_vacancies.csv"


def test_add_and_load_vacancy(saver_csv, sample_vacancy):
    saver_csv.add_vacancy(sample_vacancy)
    vacancies = saver_csv.load()
    assert len(vacancies) == 1
    assert vacancies[0].title == sample_vacancy.title
    assert vacancies[0].url == sample_vacancy.url
    assert vacancies[0].salary == sample_vacancy.salary
    assert vacancies[0].description == sample_vacancy.description


def test_delete_vacancy(saver_csv, sample_vacancy):
    saver_csv.add_vacancy(sample_vacancy)
    saver_csv.add_vacancy(Vacancy("Other", "https://other.com", 50000, "Other desc"))
    saver_csv.delete_vacancy(sample_vacancy)
    remaining = saver_csv.load()
    assert len(remaining) == 1
    assert remaining[0].title == "Other"


def test_load_with_missing_file():
    missing_saver = CSVSaver(path="nonexistent.csv")
    vacancies = missing_saver.load()
    assert vacancies == []


def teardown_function():
    if os.path.exists(TEST_CSV_PATH):
        os.remove(TEST_CSV_PATH)
