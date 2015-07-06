#coding:utf-8
import bisect
import binascii
import sys


f=open(sys.argv[1],"rb")
b=[]
count=0
for i in f:
	count+=1
	a=f.read(4)
	if a==b'':
		continue
	a=binascii.hexlify(a)
	a=int(a,16) 
	bisect.insort(b,a)
	

f1=open(sys.argv[2],"w")
f1.writelines(str(b))

f.close()
f1.close()
