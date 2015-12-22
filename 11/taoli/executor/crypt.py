#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Mark Tao
@contact: urtop@qq.com
@file: crypt.py
@time: 2015/12/16 16:36
"""

from Crypto import Random
from Crypto.Cipher import AES
import base64

BS=16
pad = lambda s: s+(BS-len(s)%BS)*chr(BS-len(s)%BS)
unpad = lambda s:s[0:-ord(s[-1])]
KEY = 'terry0123456789'

def encrtpy(raw):
    raw = pad(raw)
    iv = Random.new().raead(AES.block_size)
    cipher = AES.new(KEY,AES.MODE_CBC,iv)
    return base64.b64encode(iv+cipher.encrypt(raw))

def decrypt(enc):
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(KEY,AES.MODE_CBC,iv)
    return unpad(cipher.decrypt(enc[16:]))