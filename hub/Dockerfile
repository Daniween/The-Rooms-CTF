FROM debian:12-slim

ARG USER
ARG PASS

RUN apt-get update && apt-get install -y \
    curl \
    iputils-ping \
    net-tools \
    openssh-server \
    sudo \
    zip \
    && rm -rf /var/lib/apt/lists/*

COPY hub/motd.txt /etc/motd

RUN mkdir /var/run/sshd

RUN useradd -m -s /bin/bash $USER && \
    echo "$USER:$PASS" | chpasswd && \
    usermod -aG sudo $USER

WORKDIR /home/$USER

RUN mkdir docs && chown $USER:$USER docs && chmod 700 docs
COPY docs/resources/ docs/

COPY hub/briefing.txt briefing.txt

RUN chown -R $USER:$USER /home/$USER && chmod -R 700 /home/$USER

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]