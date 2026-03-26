#!/bin/bash
# Start background web server
cd /opt/internal_api && nohup python3 -m http.server 8080 -b 127.0.0.1 > /dev/null 2>&1 &
# Start sshd
/usr/sbin/sshd -D
