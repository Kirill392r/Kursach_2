from src.vacancy import Vacancy


def test_add_and_load_vacancy(saver_txt, sample_vacancy):
    saver_txt.add_vacancy(sample_vacancy)
    vacancies = saver_txt.load()

    assert len(vacancies) == 1
    assert vacancies[0].title == sample_vacancy.title
    assert vacancies[0].url == sample_vacancy.url
    assert vacancies[0].salary == sample_vacancy.salary
    assert vacancies[0].description == sample_vacancy.description


def test_delete_vacancy(saver_txt, sample_vacancy):
    another_vacancy = Vacancy(
        title="FastAPI Developer",
        url="https://example.com/job2",
        salary=120000,
        description="Backend project",
    )

    saver_txt.add_vacancy(sample_vacancy)
    saver_txt.add_vacancy(another_vacancy)

    saver_txt.delete_vacancy(sample_vacancy)
    vacancies = saver_txt.load()

    assert len(vacancies) == 1
    assert vacancies[0].title == another_vacancy.title
    assert vacancies[0].url == another_vacancy.url
