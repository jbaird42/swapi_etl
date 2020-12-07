FROM python:3.7 AS app

WORKDIR /app

RUN pip install pipenv

COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv install --dev

ADD . /app

ENTRYPOINT ["pipenv", "run"]

CMD [ "nosetests", "-c", "test_setup.cfg"]