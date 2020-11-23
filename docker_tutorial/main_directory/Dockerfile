FROM python:3.6-stretch
SHELL ["/bin/bash", "-l", "-c"]

WORKDIR /app
COPY app /app
ADD requirements.txt /app
RUN pip3 install --upgrade pip && \
    pip3 install --upgrade setuptools && \
    pip3 install -r requirements.txt

CMD ["uWSGI", "--http", "0.0.0.0:9090", "--wsgi-file", \
    "/app/main.py", "--callable", "app", "--stats", "0.0.0.0:9191"]