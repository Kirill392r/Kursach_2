import pytest

from src.csv_saver import CSVSaver
from src.json_saver import JSONSaver
from src.txt_saver import TXTSaver
from src.vacancy import Vacancy


@pytest.fixture
def sample_response():
    return {
        "items": [
            {
                "id": "1",
                "name": "Python Developer",
                "snippet": {"requirement": "Опыт с Python"},
            },
            {
                "id": "2",
                "name": "Backend Developer",
                "snippet": {"requirement": "Опыт с Django"},
            },
        ]
    }


@pytest.fixture
def sample_vacancies():
    return [
        Vacancy(
            "Senior Python Developer", "http://example.com/1", 120000, "Remote position"
        ),
        Vacancy(
            "Junior Python Developer", "http://example.com/2", 60000, "Junior position"
        ),
        Vacancy(
            "Python Developer with Data Analysis",
            "http://example.com/3",
            90000,
            "Requires Python and Data skills",
        ),
    ]


@pytest.fixture
def sample_vacancy():
    return Vacancy(
        title="Python Developer",
        url="https://example.com/job1",
        salary=100000,
        description="Awesome Python job",
    )


@pytest.fixture
def saver_csv(tmp_path):
    file_path = tmp_path / "vacancies.csv"
    return CSVSaver(path=str(file_path))


@pytest.fixture
def saver_json(tmp_path):
    file_path = tmp_path / "vacancies.json"
    return JSONSaver(path=str(file_path))


@pytest.fixture
def saver_txt(tmp_path):
    file_path = tmp_path / "vacancies.txt"
    return TXTSaver(path=str(file_path))
