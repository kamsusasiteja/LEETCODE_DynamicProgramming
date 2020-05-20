#houserbber(no adjacent houses to be stolen)
l=[6, 7, 1, 3, 8, 2, 4] 
#dp=[6,7,7,10,15,15,19]
n=len(l)
# dp=[0]*n
def loot(l,n):
    if n==0:
        return 0
    if n==1:
        return l[0]
    if n==2:
        return max(l1[0],l1[1])
    dp=[0]*n
    dp[0]=l[0]
    dp[1]=max(l[0],l[1])
    for i in range(2,n):
        dp[i]=max(l[i]+dp[i-2],dp[i-1])
    
    return dp[-1]
print(loot(l,n))    
