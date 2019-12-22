m=int(input())
n=list(map(int,input().split()))[:m]
sum=n[m-1]+n[m-2]+n[m-3]
for i in n:
  print(i-sum,end=" ")
