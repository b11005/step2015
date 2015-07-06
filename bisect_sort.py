#coding:utf-8
import bisect
import binascii


f=open("test100","rb")
b=[]
count=0
for i in f:
	count+=1
	a=f.read(4)
	if a==b'':
		continue
	a=binascii.hexlify(a)
	a=int(a,16)
	#if b==[]: b.append(a)
	#else: 
	bisect.insort(b,a)
	'''for j in range(count-1):
		if b==[]: b.append(a)
		elif a>=b[j]:
			b.append(a)
		else:
			b.bisect.insort(0,a)'''

f1=open("result100","w")
#for i in range(len(b)):
f1.writelines(str(b))
	#print(b[i])
f.close()
f1.close()
