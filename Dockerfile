FROM python:3.8

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY ./flask_01 ./flask_01

CMD ["python", "./flask_01/app.py"]
