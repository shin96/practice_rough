def get_fibo(n, memo={}):
    if n in memo: return memo[n]
    if n <= 2: return 1
    memo[n] = get_fibo(n - 1) + get_fibo(n - 2)
    return memo[n]

print(get_fibo(50))

0, 1, 1, 2, 3, 5, 8