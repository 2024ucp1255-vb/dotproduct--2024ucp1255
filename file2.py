import numpy as np
def vectordot(v1,v2):
	n=len(v1)
	s=0.0
	for i in range(0,n):
		s+=v1[i]*v2[i]
	return s


v1=[]
v2=[]

n=int(input("Enter vector size:"))
print("Enter v1")
for i in range(n):
	a=float(input())
	v1.append(a)
print("Enter v2")
for i in range(n):
	a=float(input())
	v2.append(a)

print("Dot product: ",vectordot(v1,v2))
