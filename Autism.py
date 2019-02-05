import numpy as np
T = int(input())
for i in range(T):
N=int(input())
A=np.zeros((N,N))
t=0
i=1
while t<=2*N-2:
 for x in range(N):
     for y in range(N):
       if(x+y==t):
          A[x][y]=i
            i+=1
            t+=1
for z in range(int(N)):
print(" ".join(str(int(x)) for x in A[z]))
