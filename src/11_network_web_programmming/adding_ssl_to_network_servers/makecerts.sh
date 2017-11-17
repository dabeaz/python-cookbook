#!/bin/sh

openssl req -new -x509 -days 365 -nodes -out server_cert.pem -keyout server_key.pem
openssl req -new -x509 -days 365 -nodes -out client_cert.pem -keyout client_key.pem
