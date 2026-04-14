class Solution:
    def fib(self, n: int) -> int:
        l=[0,1]
        for i in range(1,n):
            l.append(l[i]+l[i-1])
        return l[n]