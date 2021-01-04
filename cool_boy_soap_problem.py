def bs(arr, l, h, k):
    while l <= h:
        m = l + ((h-l) >> 1)
        if arr[m] >= k:
            h = m - 1
        else:
            l = m + 1
            
    return l
    
n = int(input())
arr = list(map(int, input().strip().split()))
arr.sort()
 
for _ in range(int(input())):
    k = int(input())
    res = bs(arr, 0, n-1, k)
    print(res)
