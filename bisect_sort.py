#coding:utf-8
import bisect
import binascii
import sys


f=open(sys.argv[1],"rb")
b=[]
count=0
for i in f:
	count+=1
	a=f.read(2)
	if a==b'':
		continue
	a=binascii.hexlify(a)
	a=int(a,16) 
	count+=1
	bisect.insort(b,a)
	
print (count)
f1=open(sys.argv[2],"w")
f1.writelines(str(b))
#f1=open(sys.argv[2],"wb")
#f1.writelines(b)

f.close()
f1.close()
