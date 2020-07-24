d={}
f=open('h.txt','r')
str=f.readline()
l=str.split()
for i in l:
    d[i]=d.get(i,0)+1
for i in d:
    print(i,d[i])
