import sys, array
f=open(sys.argv[1],'rb')
a = array.array('i', f.read())
a = list(a)
a.sort()
a = array.array('i', a)
f1=open(sys.argv[2],'wb')
a.tofile(f1)
f.close()
f1.close()