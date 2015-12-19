#!/usr/bin/env python
#coding=utf-8

import crypt


if __name__=='__main__':
    name='abcdefg'
    print "Before : %s " % name
    encode=crypt.encrypt(name)
    print "encode : %s " % encode

    decode=crypt.decrypt(encode)
    print "decode : %s " % decode
