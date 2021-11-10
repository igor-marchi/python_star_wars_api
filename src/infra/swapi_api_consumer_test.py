from .swapi_api_consumer import SwapiApiConsumer


def test_get_starships(requests_mock):
    ''' Testing get_startships mehod '''
    requests_mock.get('https://swapi.dev/api/starships/',
                      status_code=200, json={'some': 'thing'})
    swapi_api_coonsumer = SwapiApiConsumer()
    response = swapi_api_coonsumer.get_starships(page=1)

    print(response)
