from .swapi_api_consumer import SwapiApiConsumer


def test_get_starships():
    swapi_api_coonsumer = SwapiApiConsumer()
    page = 1
    get_starships_response = swapi_api_coonsumer.get_starships(page=page)

    assert get_starships_response.request.method == 'GET'
    assert get_starships_response.request.url == 'https://swapi.dev/api/starships/'
    assert get_starships_response.request.params == {'page': page}

    assert get_starships_response.status_code == 200
    assert isinstance(get_starships_response.response['results'], list)
