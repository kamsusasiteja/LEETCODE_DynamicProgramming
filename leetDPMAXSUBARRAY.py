#maximum sub array (or) Largest sum contiguos subarray
l=[-2,1,-3,4,-1,2,1,-5,4]
max_so_far = 0
max_ending_here = 0
for i in l:
    max_ending_here=max_ending_here+i
    if(max_ending_here<0):
        max_ending_here=0
    elif(max_so_far<max_ending_here):
        max_so_far=max_ending_here
print(max_so_far)