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
    curl iputils-ping net-tools openssh-server zip unzip \
    python3 python3-flask sqlite3 sqlmap \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /var/run/sshd

RUN useradd -m -s /bin/bash ${USER} && \
    echo "${USER}:${PASS}" | chpasswd

# Create the secret zip
RUN mkdir -p /tmp/secret && \
    echo "${FLAG}" > /tmp/secret/flag.txt && \
    echo "${SECRET_PART}" > /tmp/secret/key_part.txt && \
    printf "Félicitations ! Vous avez infiltré EvilCorp avec succès.\nVous avez prouvé vos compétences en cybersécurité.\nÀ bientôt pour de nouveaux défis !" > /tmp/secret/congrats.txt && \
    zip -j -P "${ZIP_PASS}" /home/${USER}/secret.zip /tmp/secret/* && \
    chown ${USER}:${USER} /home/${USER}/secret.zip && \
    rm -rf /tmp/secret

# Build the SQLite database (FLAG and ZIP_PASS baked in at build time)
RUN mkdir -p /var/db && \
    sqlite3 /var/db/ctf.db "
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary INTEGER
);
INSERT INTO employees VALUES (1,'Alice Martin','Ingenierie',85000);
INSERT INTO employees VALUES (2,'Bob Dupont','Marketing',65000);
INSERT INTO employees VALUES (3,'Carol Leroy','Finance',90000);
INSERT INTO employees VALUES (4,'Dave Bernard','Securite IT',95000);

CREATE TABLE vault (
    id INTEGER PRIMARY KEY,
    secret_name TEXT NOT NULL,
    secret_value TEXT NOT NULL
);
INSERT INTO vault VALUES (1,'FLAG','${FLAG}');
INSERT INTO vault VALUES (2,'ZIP_PASS','${ZIP_PASS}');
" && chmod 644 /var/db/ctf.db

# Deploy the vulnerable web app
COPY rooms/room-06/app.py /opt/webapp/app.py

WORKDIR /home/${USER}
COPY rooms/room-06/briefing.txt briefing.txt

COPY rooms/room-06/start.sh /start.sh
RUN chmod +x /start.sh

RUN chown -R ${USER}:${USER} /home/${USER} && chmod -R 700 /home/${USER}

EXPOSE 22
CMD ["/start.sh"]
