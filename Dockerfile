FROM python:3.8-buster

RUN groupadd -r appuser && \
    useradd --no-log-init -r -g appuser appuser && \
    mkdir -p /home/appuser && \
    chown -R appuser:appuser /home/appuser
USER appuser
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | POETRY_VERSION=1.0.0b4 python
ENV PATH="/home/appuser/.poetry/bin:${PATH}"
WORKDIR /app
COPY pyproject.toml poetry.lock /app/
RUN poetry install --no-dev --extras hosting
COPY . .
EXPOSE 8000

CMD poetry run gunicorn -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000 -w $(nproc) app.app:app