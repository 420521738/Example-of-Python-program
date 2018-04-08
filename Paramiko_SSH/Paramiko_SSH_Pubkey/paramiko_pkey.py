#!/usr/bin/env python
# --*-- coding: utf-8 --*--
import paramiko
import sys,os

host = sys.argv[1]	###ִ������ű�����ӵ�IP��ַ
user = 'ihavecar'	###����Զ�������û���
port = 22612		###����Զ�����Ӷ˿�
cmd = sys.argv[2]	###ִ������ű�����ӵ�����
pkey_file = '/root/.ssh/id_rsa'	###�������Կ��·��������
key = paramiko.RSAKey.from_private_key_file(pkey_file)	###����RSA����֤key��˽ԿΪ�ոն����pkey_file

s = paramiko.SSHClient()	###��ssh�ͻ���ʵ��
s.load_system_host_keys()	###���ر���host�����ļ�,��ͨ�û�����/home/xxx/.ssh/known_hosts

s.connect(host,port,user,pkey=key,timeout=5)	###����Զ������
stdin,stdout,stderr = s.exec_command(cmd)	###ִ�����stdin�����룬stdout�������stderr��ִ�д�����Ϣ

cmd_result = stdout.read(),stderr.read()	###��ȡִ�еĽ����ִ�в�������stderr.read()Ϊ�գ�ִ�г�����stdout.read()Ϊ��

for line in cmd_result:
	print line

s.close()