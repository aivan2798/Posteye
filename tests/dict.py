dic={}
#dic[0]="hello"
#[1]="world"

for x in range(5):
 if dic.get(x)==None:
  dic[x]=[]
  print("No key"+str(x))
 #dic[x]=
 dic[x].append(int(x+1))
# x=x+1
 
for y in range(5):
  if dic.get(y)==None:
   print("key 0")
   dic[y]=[]
  #dic[y]=
  dic[y].append(int(y+2))
#  x=x+1
 
for z in range(5):
 # lista=list(dic[z])
  print(dic[z])
 
 
 
print("syntax test")