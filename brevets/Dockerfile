FROM python:3.8
LABEL maintainer="ksattahu@uoregon.edu"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN chmod +x run_tests.sh
