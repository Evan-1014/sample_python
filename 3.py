n,m=map(int,input().split())
li=list()
# li=[[0 for _ in range(m)] for _ in range(n)]
# xiao=list()


for i in range(n):
        li.append(input())


for i in range(n):
    for j in range(m):
        if i!=0 and j!=0 and i!=n-1 and j!=m-1 and li[n][m]=='w' and li[n+1][m]!='m' and li[n+1][m+1]!='m' and li[n+1][m-1]!='m' and li[n][m+1]!='m' and li[n][m-1]!='m' and li[n-1][m]!='m' and li[n-1][m+1]!='m' and li[n-1][m-1]!='m':
            print(li[n][m])
