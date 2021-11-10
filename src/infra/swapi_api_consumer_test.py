from .swapi_api_consumer import SwapiApiConsumer


def test_get_starships():
    ''' Testing get_startships mehod '''

    swapi_api_coonsumer = SwapiApiConsumer()
    response = swapi_api_coonsumer.get_starships(page=1)

    print(response)
