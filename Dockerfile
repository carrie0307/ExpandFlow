FROM python:3.6

ADD ./ /opt/expandflow
WORKDIR /opt/expandflow

RUN chmod +x bin/manage \
  && pip install -r requirements/app.txt

CMD bin/manage start --daemon-off
