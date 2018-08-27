FROM python:latest

RUN apt-get update && \
    apt-get install -y python-pip && \
    pip install -v ptvsd==3.0.0
    
COPY ./ /app
WORKDIR /app

CMD python -u hello.py