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
    iputils-ping net-tools openssh-server zip unzip lighttpd \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /var/run/sshd

RUN useradd -m -s /bin/bash $USER && \
    echo "$USER:$PASS" | chpasswd
# Charlie won't have sudo to prevent bypassing restrictions

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

COPY rooms/room-03/motd.txt /etc/motd
RUN chmod 644 /etc/motd && echo "PrintMotd yes" >> /etc/ssh/sshd_config

WORKDIR /home/$USER
COPY rooms/room-03/briefing.txt briefing.txt

# Create local webserver files
RUN mkdir -p /opt/internal_api && \
    echo "<h1>EvilCorp Internal API</h1><p>Access Token: $ZIP_PASS</p>" > /opt/internal_api/index.html && \
    chown -R root:root /opt/internal_api && chmod -R 755 /opt/internal_api

# Minimal Lighttpd config for internal API only
RUN printf 'server.document-root = "/opt/internal_api"\n\
server.port = 8080\n\
server.bind = "127.0.0.1"\n\
index-file.names = ( "index.html" )\n\
mimetype.assign = ( ".html" => "text/html" )' > /etc/lighttpd/lighttpd.conf

# Copy init script
COPY rooms/room-03/start.sh /start.sh
RUN chmod +x /start.sh

RUN chown -R $USER:$USER /home/$USER && chmod -R 700 /home/$USER

EXPOSE 22

CMD ["/start.sh"]
