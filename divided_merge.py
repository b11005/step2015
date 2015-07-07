import sys, array, tempfile, heapq
assert array.array('i').itemsize == 4
 
def intsfromfile(f):
    while True:
        a = array.array('i')
        a.frombytes(f.read(4000))
        if not a:
            break
        for x in a:
            yield x
 
iters = []
test=open(sys.argv[1],'rb')
while True:
    a = array.array('i')
    a=test.read(40000)
    if not a:
        break
    f = tempfile.TemporaryFile()
    array.array('i', sorted(a)).tofile(f)
    f.seek(0)
    iters.append(intsfromfile(f))
 
a = array.array('i')
result=open(sys.argv[2], 'wb')
for x in heapq.merge(*iters):
    a.append(x)
    if len(a) >= 1000:
        a.tofile(result)
        del a[:]
if a:
    a.tofile(result)
f.close()
result.close()