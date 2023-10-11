FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /app/

COPY . /app/

WORKDIR /app

RUN apt-get update && apt-get install -y libpq-dev postgresql-client sshpass

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["flask", "--app", "app", "run", "--host=0.0.0.0"]
