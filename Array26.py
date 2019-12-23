n,k=map(int,input().split())
a=list(map(int,input().split()))[0:n]
for i in a:
  if(a[i]==k):
    print('yes')
    break
  else:
    print('no')
