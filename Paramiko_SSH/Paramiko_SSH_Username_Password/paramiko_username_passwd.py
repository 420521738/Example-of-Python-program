#!/usr/bin/env python
# --*-- coding: utf-8 --*--
import paramiko
import sys,os

host = sys.argv[1]	###ִ������ű�����ӵ�IP��ַ
user = 'ihavecar'	###�ȶ�����û���      
password = 'x+y-z=71'	###�ȶ��������
cmd = sys.argv[2]	###ִ������ű�����ӵ�����

s = paramiko.SSHClient()	###��ssh�ͻ���ʵ��
s.load_system_host_keys()	###���ر���host�����ļ�,��ͨ�û�����/home/xxx/.ssh/known_hosts
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())	###��һ��Զ�̻���ʾ����yes�����������䣬��һ��ͨ��paramikoԶ�̴����ʱ��ͻ����

s.connect(host,22612,user,password,timeout=5)	###����Զ������
stdin,stdout,stderr = s.exec_command(cmd)	###ִ�����stdin�����룬stdout�������stderr��ִ�д�����Ϣ

cmd_result = stdout.read(),stderr.read()	###��ȡִ�еĽ����ִ�в�������stderr.read()Ϊ�գ�ִ�г�����stdout.read()Ϊ��

for line in cmd_result:
	print line

s.close()
