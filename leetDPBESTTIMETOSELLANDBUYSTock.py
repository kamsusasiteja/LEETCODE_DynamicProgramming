#Best Time to Buy and Sell Stock(maximum profit)
l=[7,1,5,3,6,4]
maxx=0
minn=1000
for i in l:
    if i<minn:
        minn=i
    else:
        maxx=max(maxx,i-minn)
print(maxx)