FROM python:3.12

RUN mkdir /app/

COPY . /app/

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["flask", "--app", "app", "run", "--host=0.0.0.0"]
