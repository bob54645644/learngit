import datetime
import time
import shutil
import re
from email.mime.text import MIMEText
import smtplib
temp=re.compile(r'\d+.\d+.\d+.\d+ - - \[\d{2}/\w+/\d{4}:\d{2}:\d{2}:\d{2} \+\d{4}\] "(\w+ /.*) HTTP.*" .*')
baktime=datetime.datetime.now()+datetime.timedelta(days=1)
baktime=str(baktime)[:10]+' 00:00:00'

temptime=str(datetime.datetime.now())[:10]+' 23:55:00'

#
def backup():
	shutil.copy('/home/bob/nginx/logs/access.log','./logs/{}.log'.format(temptime[:10]))
	with open('/home/bob/nginx/logs/access.log','w') as f:
		f.write('')

#tongji
def tongji(date):
	with open('/home/bob/python/venv/logs/'+date+'.log') as f:
		txt=f.readlines()
	llist=[]
	for i in txt:
		te=temp.findall(i)[0]
		if te:
			llist.append(te)
	l=list(set(llist))
	numb=[]
	for i in l:
		numb.append(llist.count(i))
	dic={}
	for i in range(len(l)):
		dic[l[i]]=numb[i]
	dic=sorted(dic.items(),key=lambda key:key[1],reverse=True)
	ll=[]
	for i,j in dic:
		if len(ll)<10:
			ll.append(i)
	return ll

#sendmail
password=input('password:')
def sendmail(password,llist):
	ms=''
	for  i in llist:
		ms=ms+i+' \n '
	msg=MIMEText(ms,'plain','utf-8')
	server=smtplib.SMTP('smtp.163.com',25)
	#server.starttls()
	server.set_debuglevel(1)
	server.login('15637589942@163.com',password)
	server.sendmail('15637589942@163.com',['15637589942@163.com'],msg.as_string())
	server.quit()



while True:
	now=str(datetime.datetime.now())[:19]
	if now < temptime:
		time.sleep(180)
	else:
		if now < baktime:
			time.sleep(1)
		else:
			backup()
			print('{}backup'.format(baktime))

			#tongji
			date=temptime[:10]
			llist=tongji(date)

			#sendmail
			sendmail(password,llist)
			print('sendmail ok')
			
			temptime=str(datetime.datetime.now())[:10]+' 23:55:00'
			baktime=datetime.datetime.now()+datetime.timedelta(days=1)
			baktime=str(baktime)[:10]+' 00:00:00'








