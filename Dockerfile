FROM ubuntu:18.04
MAINTAINER Philipp Braun, 3589810@gmail.com

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
    build-essential \
    ca-certificates \
    gcc \
    git \
    libpq-dev \
    libdb++-dev \
    make \
    python-pip \
    python3-pip \
    python2.7 \
    python2.7-dev \
    ssh \
    && apt-get autoremove \
    && apt-get clean

RUN apt-get update \
  && apt-get install -y git \
                        vim \
                        g++ \
                        make \
                        wget

RUN pip install ecdsa pandas
RUN pip3 install ecdsa pandas
RUN export BERKELEYDB_DIR=/usr \
    && pip install bsddb3
RUN export BERKELEYDB_DIR=/usr \
    && pip3 install bsddb3