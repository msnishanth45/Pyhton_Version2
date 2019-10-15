n=int(input())
m=n
sum=0
prd=1
while(n>0):
  r=n%10
  sum=sum+r
  prd=prd*r
  n=n//10
temp=sum + prd
if(temp==m):
  print('Great')
else:
  print('no')
