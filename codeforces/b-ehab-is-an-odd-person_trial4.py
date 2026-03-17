n = int(input())
arr = list(map(int, input().split()))

evenodd = [False, False]
for i in arr:
    evenodd[i % 2] = True

if evenodd[0] and evenodd[1]:
    arr.sort()
print(*arr)