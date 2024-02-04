FROM python:3.12.0-slim-bookworm

# Set Working Directory
ENV HOME="/root"
WORKDIR ${HOME}

ENV PATH="/etc/poetry/bin:${PATH}"

#-----------------------------------------------------------------------------
# Setup OS and install system dependencies
# Note:
#   - mecab, mecab-ipadic-utf8, libmecab-dev are required for mecab-python3
#----------------------------------------------------------------------------
RUN apt-get update -y &&\
    apt-get install -y \
      build-essential \
      curl \
      file \
      git \
      gcc \
      libpq-dev \
      libmariadb-dev \
      pkg-config \
      python3-dev \
      sudo

#----------------------------------------------------------------------------
# Install Poetry for Python package management
#----------------------------------------------------------------------------

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/etc/poetry python3 -
