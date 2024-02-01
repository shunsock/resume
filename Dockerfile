FROM python:3.10-slim-bookworm

# Set Working Directory
ENV HOME="/root"
WORKDIR ${HOME}

# Install Dependencies
RUN apt-get update && \
  apt-get install -y --no-install-recommends \
  curl \
  make

# Install pip and pip-tools
RUN python -m pip install --upgrade pip && \
    pip install pip-tools

# Download and execute the Rye installation script
RUN curl -sSf https://rye-up.com/get | RYE_VERSION="0.20.0" RYE_INSTALL_OPTION="--yes" bash

# Add Rye environment to bashrc for future sessions
RUN echo 'source "$HOME/.rye/env"' >> ~/.bashrc
