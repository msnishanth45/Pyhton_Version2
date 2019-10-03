x=input()
k=0
for i in x:
  if(ord(i)==97 or 101 or 105 or 111 or 117):
    k=k+ord(i)
    if(k%8==0):
      print('1')
      if(k%8!=0):
        print('0')
        
      
