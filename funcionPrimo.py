import sys
n=long(sys.argv[1])
i=2
r=1
while i<n and r>0:
 r=n%i;i+=1
print r
