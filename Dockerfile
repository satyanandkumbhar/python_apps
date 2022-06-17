FROM python:3.8

WORKDIR /app

COPY ./flask_01/requirements.txt .

RUN pip3 install -r requirements.txt

COPY ./flask_01 .

CMD ["python", "app.py"]
