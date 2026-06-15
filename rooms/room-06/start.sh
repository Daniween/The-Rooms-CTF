#!/bin/bash
python3 /opt/webapp/app.py &
exec /usr/sbin/sshd -D
