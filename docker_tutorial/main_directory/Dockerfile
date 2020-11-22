FROM python:3.6-stretch
SHELL ["/bin/bash", "-l", "-c"]

WORKDIR /app
COPY app /app
ADD requirements.txt /app
RUN pip install -r requirements.txt

CMD ["python", "main.py"]