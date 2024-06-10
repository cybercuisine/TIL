import sys
input = sys.stdin.readline

N,M,Q=map(int,input().split())
A=list(map(int,input().split()))

mod=10**9+7

def compose(X,a):
    DP=[0]*2001
    for i in range(2001):
        if X[i]!=0:
            DP[i]+=X[i]
            if i+a+1<2001:
                DP[i+a+1]-=X[i]

    DP[0]%=mod

    for i in range(1,2001):
        DP[i]=(DP[i]+DP[i-1])%mod

    return DP
            
            

NOW=[0]*2001
NOW[0]=1

for i in range(N):
    NOW=compose(NOW,A[i])


ANS=[[] for i in range(N)]

for i in range(N):
    DP=[0]*2001

    a=A[i]
    S=[0]*2001

    for j in range(2001):
        DP[j]=NOW[j]
        if j-1>=0:
            DP[j]-=S[j-1]
        if j-a-1>=0:
            DP[j]+=S[j-a-1]

        S[j]=(S[j-1]+DP[j])%mod

    ANS[i]=tuple(DP)    

for tests in range(Q):
    k,x=map(int,input().split())

    k-=1
    print(ANS[k][M-x]%mod)
        
