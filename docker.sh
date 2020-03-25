#! /bin/bash

docker build -t hansen1416/networkx:latest .
# $(id -u):$(id -g) current user id and group id
#docker run -itd --name qingyun_server --user $(id -u):$(id -g) hansen1416/qingyun_server:1.0

docker run -itd --name networkx \
--mount type=bind,source=/home/hlz/networkx,target=/mnt/code \
hansen1416/networkx:latest
