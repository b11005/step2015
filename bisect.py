#coding:utf-8
import binascii
#from io import BytesIO

f=open("test1","rb")
b=[]
count=0
for i in f:
	count+=1
	a=f.read(4)
	if a==b'':
		continue
	for j in range(count-1):
		if b==[]: b.append(a)
		elif a>=b[j]:
			b.append(a)
		else:
			b.insert(0,a)
	'''a=binascii.hexlify(a)
	a=int(a,16)
	print (a)
	b.append(a)'''
f1=open("result1","wb")
for i in range(len(b)):
	f1.write(b[i])


f.close()
f1.close()
