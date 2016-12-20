FROM python:3.5

COPY config/requirements.txt /config/requirements.txt

RUN pip install -r config/requirements.txt

WORKDIR config

CMD python make_config_file.py


