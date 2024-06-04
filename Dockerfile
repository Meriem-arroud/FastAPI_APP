FROM python:3.11

WORKDIR /code

COPY . /code

RUN cd /code
RUN pip install --no-cache-dir --upgrade pipenv
RUN pipenv install

CMD ["pipenv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port 8080"]
