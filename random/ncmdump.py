#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


import base64
import binascii
import json
import os
import struct

from Crypto.Cipher import AES


def parse_file(file_path):
    core_key = binascii.a2b_hex("687A4852416D736F356B496E62617857")
    meta_key = binascii.a2b_hex("2331346C6A6B5F215C5D2630553C2728")
    unpad = lambda s: s[0:-(s[-1] if type(s[-1]) == int else ord(s[-1]))]

    with open(file_path, 'rb') as f:
        header = f.read(8)
        assert binascii.b2a_hex(header) == b'4354454e4644414d'
        f.seek(2, 1)  # magic number.

        # key_box is used to decode audio data.
        key_length = f.read(4)
        key_length = struct.unpack('<I', bytes(key_length))[0]
        key_data = f.read(key_length)
        key_data_array = bytearray(key_data)
        for i in range(0, len(key_data_array)):
            key_data_array[i] ^= 0x64
        key_data = bytes(key_data_array)
        cryptor = AES.new(core_key, AES.MODE_ECB)
        key_data = unpad(cryptor.decrypt(key_data))[17:]
        key_length = len(key_data)
        key_data = bytearray(key_data)
        key_box = bytearray(range(256))
        last_byte = 0
        key_offset = 0
        for i in range(256):
            swap = key_box[i]
            c = (swap + last_byte + key_data[key_offset]) & 0xff
            key_offset += 1
            if key_offset >= key_length:
                key_offset = 0
            key_box[i] = key_box[c]
            key_box[c] = swap
            last_byte = c

        # meta data
        meta_length = f.read(4)
        meta_length = struct.unpack('<I', bytes(meta_length))[0]
        meta_data = f.read(meta_length)
        meta_data_array = bytearray(meta_data)
        for i in range(0, len(meta_data_array)):
            meta_data_array[i] ^= 0x63
        meta_data = bytes(meta_data_array)
        meta_data = base64.b64decode(meta_data[22:])
        cryptor = AES.new(meta_key, AES.MODE_ECB)
        meta_data = unpad(cryptor.decrypt(meta_data)).decode('utf-8')[6:]
        meta_data = json.loads(meta_data)

        # crc32
        crc32 = f.read(4)
        crc32 = struct.unpack('<I', bytes(crc32))[0]

        # image data.
        f.seek(5, 1)
        image_size = f.read(4)
        image_size = struct.unpack('<I', bytes(image_size))[0]
        image_data = f.read(image_size)

        audio_data = bytearray()
        while True:
            chunk = bytearray(f.read(0x8000))
            chunk_length = len(chunk)
            if not chunk:
                break
            for i in range(1, chunk_length + 1):
                j = i & 0xff
                chunk[i - 1] ^= key_box[(key_box[j] + key_box[(key_box[j] + j) & 0xff]) & 0xff]
            audio_data.extend(chunk)

        # print(meta_data, crc32)
        return meta_data, crc32, image_data, audio_data


def run_file(file_path, output_path):
    meta_data, _, _, audio_data = parse_file(file_path)
    with open(output_path, 'wb') as m:
        m.write(audio_data)


def handle_files(file_dir):
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            ext = os.path.splitext(file)[1]
            output = os.path.splitext(file)[0] + '.mp3'
            if ext == '.ncm' and not os.path.exists(output):
                print('[%s] -> [%s]' % (file, output))
                run_file(file, output)


def main():
    cwd = os.getcwd()
    print(cwd)
    handle_files(cwd)


if __name__ == '__main__':
    main()
