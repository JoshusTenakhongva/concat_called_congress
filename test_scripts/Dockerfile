FROM python:3.9.12-slim-bullseye

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . . 

CMD [ "python", "./test.py" ]