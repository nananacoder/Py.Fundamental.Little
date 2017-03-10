#!/usr/bin/env python2.7
# -*-coding:utf-8-*-

import hashlib

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def db_encrypt(table):
    '''
    md5 encryption in database
    :param table:
    :return:

    '''
    sql = "INSERT INTO m_tbbackup(id,sName,password) VALUES (1,'yanganqi',AES_ENCRYPT('123456','yaq'));"
    extract = "SELECT id,sNAME,AES_DECRYPT(password,'yaq') as password FROM tmp3 WHERE sName='yanganqi';"

