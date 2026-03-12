x,y = map(int,input().split())
arr = list(map(int,input().split()))
left = 0
curr = 0
maxs = 0
for right in range(x):
    curr += arr[right]
    while curr > y:
        curr -= arr[left]
        left += 1
    maxs = max(maxs, right - left + 1)
print(maxs)