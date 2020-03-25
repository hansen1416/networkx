FROM python:3.7-buster

RUN pip install networkx matplotlib scipy

WORKDIR /mnt/code