# cat paramiko_pkey_sftp.py
#!/usr/bin/env python
# --*-- coding: utf-8 --*--
import paramiko
import sys,os

host = sys.argv[1]		###ִ������ű�����ӵ�IP��ַ
user = 'ihavecar'
port = 22612			###����ö˿�
pkey_file = '/root/.ssh/id_rsa'	###�������Կ��·��������
key = paramiko.RSAKey.from_private_key_file(pkey_file)	###����RSA����֤key��˽ԿΪ�ոն����pkey_file

t = paramiko.Transport((host,port))		###�󶨴���ʵ��t
t.connect(username=user,pkey=key)	###����һ����������

sftp = paramiko.SFTPClient.from_transport(t)	###����һ��sftpʵ������tʵ����ȡ
sftp.get('/home/ihavecar/1.txt','1.new.txt')	###��Զ�̷�������/home/ihavecar/1.txt���ص���ǰ·�������������ļ�Ϊ1.new.txt
sftp.put('1.new.txt','/tmp/1.txt')		###����ǰ·���µ�1.new.txt�ϴ���Զ�̷�������/tmp/�£���������Ϊ1.txt

t.close()