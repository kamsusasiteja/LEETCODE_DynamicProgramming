#DP Climbing stairs
def fibn(n):
    if n<=1:
        return n
    return fibn(n-1) + fibn(n-2)
def countstairs(n):
    return fibn(n+1)
n=int(input())
print(countstairs(n))