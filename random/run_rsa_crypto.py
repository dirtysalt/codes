#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import base64
import os

from Crypto.PublicKey import RSA

# random_generator = Random.new().read
# key = RSA.generate(1024, random_generator)

private_key_data = open(os.environ['HOME'] + '/.ssh/id_rsa').read()
public_key_data = open(os.environ['HOME'] + '/.ssh/id_rsa.pub').read()
private_key = RSA.importKey(private_key_data)
public_key = RSA.importKey(public_key_data)

plain_text = 'hello this is plain text'
encrypt_data = public_key.encrypt(plain_text.encode('utf_8'), 42)[0]
b64_data = base64.b64encode(encrypt_data).decode('utf_8')
print(b64_data)

back_encrypt_data = base64.b64decode(b64_data.encode('utf_8'))
plain_bytes = private_key.decrypt(back_encrypt_data)
back_plain_text = plain_bytes.decode('utf_8')
print(back_plain_text)
