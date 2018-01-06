import requests
import random
llist=['','apple','pear','apricot','peach','grape',\
	'banana','pineapple','plum','watermelon','orange',\
	'lemon','mango','strawberry','medlar','mulberry',\
	'nectarine','cherry','pomegranate','fig','tangerine']
for i in range(100):
	num=random.randint(0,20)
	if llist[num]:
		r=requests.get('http://127.0.0.1/user/'+llist[num],timeout=10)
	else:
		r=requests.get('http://127.0.0.1',timeout=10)
	#print(r)
