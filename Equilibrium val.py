def eq_val(n):
    arr=[1]*n + [n] + [1]*n
    size=len(arr)

    for i in range(size):
        left_sum=0
        right_sum=0
        for k in range(i):
            left_sum+=arr[k]
        for j in range(i+1,size):
            right_sum+=arr[j]
        if left_sum==right_sum:
            return arr[i]
    return -1

print("arr or 5",eq_val(5))
print("arr or 6",eq_val(6))