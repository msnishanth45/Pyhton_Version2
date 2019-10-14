def ComputeGcd(a,b):
  if(b==0):
    return -1 
  else:
    return ComputeGcd(b,a%b)

n,m=map(int,input().split())
print(ComputeGcd(n,m))
