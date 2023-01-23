#!/usr/bin/env bash
# Copyright (C) dirlt

mkdir -p /tmp/nginx_upload_files
mkdir -p /tmp/nginx_upload_state_store
cp server.conf /usr/local/etc/nginx/servers/upload.conf
sudo nginx -s reload
