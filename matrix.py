import sys
import random
allowed=set("gcta")
a=input("word 1:")
b=input("word 2:")
if(len(a)!=16 or len(b)!=16):
    sys.exit()
    
s1=[i for i in a]
s2=[i for i in b]
random.shuffle(s1)
random.shuffle(s2)
print(s1)
print(s2)

g1=[]
g2=[]
for i in range(16):
    if(not s1[i] in g1):
        g1.append(s1[i])
    if(not s2[i] in g2):
        g2.append(s2[i])
        
print(g1)
print(g2)

rows=5
cols=5

mat=[[0 for i in range(cols)] for i in range(rows)]

def matmul(mat,i,j,g1,g2):
    if(g1[i-1]==g2[j-1]):
        mat[i][j]=2+mat[i-1][j-1]
    else:
        p=max(mat[i-1][j],mat[i][j-1],mat[i-1][j-1])
        mat[i][j]=p-1
    if(i<4):
        matmul(mat,i+1,j,g1,g2)
    else:
        if(j<4):
            matmul(mat,1,j+1,g1,g2)
matmul(mat,1,1,g1,g2)

for i in range(5):
        print(mat[i])

name=[]
def trackback(mat,i,j,g1,g2,name):
    if(mat[i-1][j-1]==(mat[i][j]-5)):
        name.append(g1[i-1])
        trackback(mat,i-1,j-1,g1,g2,name)
    elif(mat[i-1][j-1]==(mat[i][j]+4)):
        name.append("_")
        name.append(g1[i-1])
        trackback(mat,i-1,j-1,g1,g2,name)
    elif(mat[i-1][j]==(mat[i][j]+4)):
        name.append("_")
        name.append(g1[i-1])
        trackback(mat,i-1,j,g1,g2,name)
    elif(mat[i][j-1]==mat[i][j]+4):
        name.append("_")
        name.append(g2[j-1])
        trackback(mat,i,j-1,g1,g2,name)
    else:
        return 
    
trackback(mat,4,4,g1,g2,name)
print(name[::-1])
    
