# docker build -t anya . && docker run -d --name anya -p 1024:1024 --rm -it anya
FROM ubuntu:20.04

RUN apt-get update
RUN apt install python3 -y
RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd
 
WORKDIR /home/ctf
COPY ./distribute/maze ./maze
COPY ./distribute/flag.txt .
COPY ./distribute/chall.py .
RUN chmod +x chall.py
COPY ./distribute/ynetd .
RUN chmod +x ynetd
COPY ./distribute/run.sh .
RUN chmod +x run.sh
RUN chown -R root:root /home/ctf/

USER ctf
CMD ./run.sh