FROM debian:12-slim

ARG USER
ARG PASS
ARG ZIP_PASS
ARG FLAG
ARG SECRET_PART
ARG NEXT_HOST=""
ARG NEXT_USER=""
ARG NEXT_PASS=""

RUN apt-get update && apt-get install -y \
    curl iputils-ping net-tools openssh-server sudo zip unzip \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /var/run/sshd

RUN useradd -m -s /bin/bash $USER && \
    echo "$USER:$PASS" | chpasswd

# No sudo for this user! We do not add the user to sudo group intentionally.

# Create the secret zip file
RUN mkdir -p /tmp/secret && \
    echo "$FLAG" > /tmp/secret/flag.txt && \
    echo "$SECRET_PART" > /tmp/secret/key_part.txt && \
    if [ -n "$NEXT_HOST" ] && [ -n "$NEXT_USER" ] && [ -n "$NEXT_PASS" ]; then \
        printf "=== Accès niveau suivant ===\nHost : %s\nUser : %s\nPass : %s\n" \
            "$NEXT_HOST" "$NEXT_USER" "$NEXT_PASS" > /tmp/secret/next_level.txt; \
    fi && \
    zip -j -P "$ZIP_PASS" /home/$USER/secret.zip /tmp/secret/* && \
    chown $USER:$USER /home/$USER/secret.zip && \
    rm -rf /tmp/secret

WORKDIR /home/$USER
COPY rooms/room-05/briefing.txt briefing.txt

# Create the SUID challenge
RUN mkdir -p /root/flag_dir && \
    echo "$ZIP_PASS" > /root/flag_dir/password.txt && \
    chmod 700 /root/flag_dir

# Copy 'find' and set SUID bit to create the vulnerability
RUN cp /usr/bin/find /usr/local/bin/find && \
    chmod 4755 /usr/local/bin/find

RUN chown -R $USER:$USER /home/$USER && chmod -R 700 /home/$USER

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
