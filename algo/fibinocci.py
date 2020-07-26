def get_Nth_fibonacci(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return get_Nth_fibonacci(n-1) + get_Nth_fibonacci(n-2)

n = 8
for i in range(1, n+1):
    print(get_Nth_fibonacci(i))