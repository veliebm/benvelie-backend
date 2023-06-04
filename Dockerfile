FROM python:3.11

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT flask --app app run --host=0.0.0.0
