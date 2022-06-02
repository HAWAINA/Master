FROM python:3.10.4

RUN mkdir -p /opt/services/beuty
WORKDIR /opt/services/beuty

RUN mkdir -p /opt/services/beuty/requirements

ADD requirements.txt /opt/services/beuty/

COPY . /opt/services/beuty/

RUN pip install -r requirements.txt
