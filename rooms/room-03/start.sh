#!/bin/bash
# Start background web server (Lighttpd)
lighttpd -f /etc/lighttpd/lighttpd.conf &
# Start sshd
/usr/sbin/sshd -D
