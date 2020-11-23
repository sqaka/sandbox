FROM python:3.6-stretch
SHELL ["/bin/bash", "-l", "-c"]

RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi

WORKDIR /app
COPY app /app
COPY cmd.sh /

ADD requirements.txt /app
RUN pip3 install --upgrade pip && \
    pip3 install --upgrade setuptools && \
    pip3 install -r requirements.txt

EXPOSE 9090 9191
USER uwsgi

CMD ["/cmd.sh"]