class DummyData:

    @staticmethod
    def dummy_people_resources():
        return [
            {
                "name": "Test 1",
                "height": "196",
                "films": [
                    "http://swapi.dev/api/films/1/",
                    "http://swapi.dev/api/films/2/",
                    "http://swapi.dev/api/films/3/"
                ],
                "species": [
                    "http://swapi.dev/api/species/1/"
                ],
                "url": "http://swapi.dev/api/people/1/"
            },
            {
                "name": "Test 2",
                "height": "300",
                "homeworld": "http://swapi.dev/api/planets/1/",
                "films": [
                    "http://swapi.dev/api/films/1/",
                    "http://swapi.dev/api/films/2/"
                ],
                "species": [],
                "url": "http://swapi.dev/api/people/2/"
            },
            {
                "name": "Test 3",
                "height": "200",
                "homeworld": "http://swapi.dev/api/planets/1/",
                "films": [
                    "http://swapi.dev/api/films/1/",
                    "http://swapi.dev/api/films/3/"
                ],
                "species": [],
                "url": "http://swapi.dev/api/people/2/"
            },
            {
                "name": "Test 4",
                "height": "250",
                "homeworld": "http://swapi.dev/api/planets/1/",
                "films": [
                    "http://swapi.dev/api/films/1/"
                ],
                "species": [],
                "url": "http://swapi.dev/api/people/4/"
            }
        ]

    @staticmethod
    def dummy_species_resources():
        return [{"name": "human"}]

    @staticmethod
    def films_results():
        return [
            {
                "title": "Movie 1",
                "characters": [
                    "http://swapi.dev/api/people/1/",
                    "http://swapi.dev/api/people/2/",
                    "http://swapi.dev/api/people/3/",
                    "http://swapi.dev/api/people/5/"
                ],
                "url": "http://swapi.dev/api/films/1/"
            },
            {
                "title": "Movie 2",
                "characters": [
                    "http://swapi.dev/api/people/1/",
                    "http://swapi.dev/api/people/2/"

                ],
                "url": "http://swapi.dev/api/films/2/"
            },
            {
                "title": "Movie 3",
                "characters": [
                    "http://swapi.dev/api/people/1/",
                    "http://swapi.dev/api/people/3/",
                    "http://swapi.dev/api/people/4/",
                ],
                "url": "http://swapi.dev/api/films/3/"
            },
        ]
