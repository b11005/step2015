#coding:utf-8
import binascii
#from io import BytesIO

f=open("test1","rb")
count=0
for i in f:
	a=f.read(4)
	if a==b'':
		continue
	a=binascii.hexlify(a)
	a=int(a,16)
	print (a)
	count+=1
print (count)

f.close()
