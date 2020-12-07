class DummyData:

    @classmethod
    def get_films(cls):
        return {
            "count": 4,
            "next": None,
            "previous": None,
            "results": cls.films_results()
        }

    @staticmethod
    def get_test_character(value):
        character = {
            "name": f"Test {value}",
            "height": f"{value}",
            "species": [
                "http://swapi.dev/api/species/1/"
            ],
            "url": f"http://swapi.dev/api/people/{value}/"
        }
        films = [
            "http://swapi.dev/api/films/1/",
            "http://swapi.dev/api/films/2/",
            "http://swapi.dev/api/films/3/",
            "http://swapi.dev/api/films/4/"
        ]
        character.update({"films": films[value % 3:]})
        return character

    @staticmethod
    def dummy_people_resources():
        return [
            {
                "name": "Test 3",
                "height": "3",
                "films": [
                    "http://swapi.dev/api/films/1/",
                    "http://swapi.dev/api/films/2/",
                    "http://swapi.dev/api/films/3/",
                    "http://swapi.dev/api/films/4/"
                ],
                "species": [
                    "http://swapi.dev/api/species/1/"
                ],
                "url": "http://swapi.dev/api/people/3/"
            },
            {
                "name": "Test 4",
                "height": "4",
                "films": [
                    "http://swapi.dev/api/films/1/",
                    "http://swapi.dev/api/films/2/",
                    "http://swapi.dev/api/films/4/"
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
                    "http://swapi.dev/api/people/4/"
                ],
                "url": "http://swapi.dev/api/films/1/"
            },
            {
                "title": "Movie 2",
                "characters": [
                    "http://swapi.dev/api/people/1/",
                    "http://swapi.dev/api/people/2/",
                    "http://swapi.dev/api/people/3/",
                    "http://swapi.dev/api/people/4/"

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
            {
                "title": "Movie 4",
                "characters": [
                    "http://swapi.dev/api/people/3/"
                ],
                "url": "http://swapi.dev/api/films/4/"
            },
        ]
