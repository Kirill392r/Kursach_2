from src.json_saver import JSONSaver
from src.vacancy import Vacancy


def test_add_and_load_vacancy(saver_json, sample_vacancy):
    saver_json.add_vacancy(sample_vacancy)
    vacancies = saver_json.load()

    assert len(vacancies) == 1
    assert vacancies[0].title == sample_vacancy.title
    assert vacancies[0].url == sample_vacancy.url
    assert vacancies[0].salary == sample_vacancy.salary
    assert vacancies[0].description == sample_vacancy.description


def test_delete_vacancy(saver_json, sample_vacancy):
    another_vacancy = Vacancy(
        title="FastAPI Developer",
        url="https://example.com/job2",
        salary=110000,
        description="Backend work",
    )

    saver_json.add_vacancy(sample_vacancy)
    saver_json.add_vacancy(another_vacancy)

    saver_json.delete_vacancy(sample_vacancy)
    vacancies = saver_json.load()

    assert len(vacancies) == 1
    assert vacancies[0].title == another_vacancy.title


def test_json_load_file_not_found(tmp_path):
    path = tmp_path / "no_file.json"
    saver = JSONSaver(path=str(path))
    assert saver.load() == []
