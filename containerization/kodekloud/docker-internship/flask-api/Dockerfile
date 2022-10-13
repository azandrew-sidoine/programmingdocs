FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN apt-get install vim curl -y

WORKDIR /home

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

RUN export FLASK_APP=app

WORKDIR /home/src/

EXPOSE 5000

CMD [ "flask","run", "--host=0.0.0.0"]

