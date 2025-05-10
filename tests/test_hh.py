from unittest.mock import Mock, patch

from src.hh import HeadHunterAPI


@patch("src.hh.requests.get")
def test_load_vacancies_success(mock_get, sample_response):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = sample_response
    mock_get.return_value = mock_response

    api = HeadHunterAPI()
    vacancies = api.load_vacancies("Python")

    assert isinstance(vacancies, list)
    assert len(vacancies) == 10
    assert vacancies[0]["name"] == "Python Developer"


@patch("src.hh.requests.get")
def test_load_vacancies_api_error(mock_get):
    mock_response = Mock()
    mock_response.status_code = 500
    mock_response.json.return_value = {"items": []}
    mock_get.return_value = mock_response

    api = HeadHunterAPI()
    vacancies = api.load_vacancies("Python")

    assert vacancies == []


@patch("src.hh.requests.get")
def test_load_vacancies_multiple_pages(mock_get, sample_response):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = sample_response
    mock_get.return_value = mock_response

    api = HeadHunterAPI()
    vacancies = api.load_vacancies("Python")

    assert len(vacancies) == 5 * len(sample_response["items"])
    assert all("name" in vacancy for vacancy in vacancies)
