def eg_mid(n):
    arr=[1]*n + [0] + [1]*n
    size=len(arr)

    for i in range(size):
        left_sum=0
        right_sum=0
        for j in range(i):
            left_sum+=arr[j]
        for k in range(i+1,size):
            right_sum+=arr[k]

        if left_sum==right_sum:
            return i
    return -1

print("arr of 5",eg_mid(5))
print("arr of 6",eg_mid(6))    
        