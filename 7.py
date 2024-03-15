k, a, s = map(int, input().split())
if a < k > s:
    print(k)
elif k < a > s:
    print(a)
elif k < s > a:
    print(s)