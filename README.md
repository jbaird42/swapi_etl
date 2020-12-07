# swapi_etl
An ETL application for the Star Wars API (https://swapi.dev). The application currently does the following:

- Collects Character data from swapi.dev
- Gets the top characters by number of film appearances
- Sort the list based on height
- build a CSV file containing columns ('name', 'species', 'height', 'appearances') 
- send that CSV file to httpbin.org/post


## How to use locally:

### Using Pipenv

`pipenv install` 

`pipenv run python main.py`

#### Running Tests:

`pipenv install --dev`

`pipenv run nosetests`

Note: You may optionally include the test_setup.cfg if you would like test coverage info.

Ex: `pipenv run nosetests -c test_setup.cfg`

-----------

### Using Docker

`docker-compose build`

`docker-compose up`

#### Running tests:

`docker-compose -f docker-compose-test.yaml build`

`docker-compose up`


 
