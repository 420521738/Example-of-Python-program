# cat paramiko_username_passwd_sftp.py
#!/usr/bin/env python
# --*-- coding: utf-8 --*--
import paramiko
import sys,os

host = sys.argv[1]	###ִ������ű�����ӵ�IP��ַ
user = 'ihavecar'	###�ȶ�����û���      
password = 'x+y-z=71'	###�ȶ��������
port = 22612		###����ö˿�

t = paramiko.Transport((host,port))		###�󶨴���ʵ��t
t.connect(username=user,password=password)	###����һ����������

sftp = paramiko.SFTPClient.from_transport(t)	###����һ��sftpʵ������tʵ����ȡ
sftp.get('/home/ihavecar/1.txt','1.new.txt')	###��Զ�̷�������/home/ihavecar/1.txt���ص���ǰ·�������������ļ�Ϊ1.new.txt
sftp.put('1.new.txt','/tmp/1.txt')		###����ǰ·���µ�1.new.txt�ϴ���Զ�̷�������/tmp/�£���������Ϊ1.txt

t.close()