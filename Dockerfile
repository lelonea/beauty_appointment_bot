FROM python:3.10-buster as base

ENV PYTHONPATH=$PYTHONPATH:/usr/src/app/

RUN apt-get update && apt-get -y upgrade && apt-get clean

WORKDIR /usr/src/app/

COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip && pip install --no-cache-dir -r /requirements.txt


FROM base as mariadb

RUN mkdir /alembic
WORKDIR /alembic

COPY src/db/alembic /alembic

ENTRYPOINT ["bash","./migrate_db.sh"]

FROM base as dev

CMD bash

FROM base as prod

COPY ./src /usr/src/app/

CMD ["python", "./main.py"]
