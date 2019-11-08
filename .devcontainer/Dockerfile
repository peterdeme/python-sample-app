FROM python:3

RUN apt-get update \
    && apt-get -y install git curl \
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | POETRY_PREVIEW=1 python

ENV PATH="/root/.poetry/bin:${PATH}"

WORKDIR /app

CMD ["/bin/bash"]
