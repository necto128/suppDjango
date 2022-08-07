FROM python:3.10

WORKDIR /var/lib/sup/data/suppDjango/

COPY . .

RUN pip install pipenv

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# установка зависимостей
COPY ./requirements.txt .
RUN python -m pip install -r requirements.txt




