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
    curl iputils-ping net-tools openssh-server sudo zip unzip git \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /var/run/sshd

RUN useradd -m -s /bin/bash $USER && \
    echo "$USER:$PASS" | chpasswd && \
    usermod -aG sudo $USER

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
COPY rooms/room-01/briefing.txt briefing.txt

# Create the git leak challenge
RUN mkdir -p project && cd project && \
    git init && \
    git config user.email "dev@evilcorp.com" && \
    git config user.name "Lead Dev" && \
    echo "This is our top secret project." > README.md && \
    git add README.md && git commit -m "Initial commit, nothing to see." && \
    echo "DATABASE_ROOT_PASSWORD=$ZIP_PASS" > .env && \
    git add .env && git commit -m "Add environment config for local testing" && \
    rm .env && git rm .env && git commit -m "Oops, removing sensitive .env file containing the password"

RUN chown -R $USER:$USER /home/$USER && chmod -R 700 /home/$USER

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
