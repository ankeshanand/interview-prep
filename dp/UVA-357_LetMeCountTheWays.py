coin_values = [1, 5, 10, 25, 50]

while True:
    try:
        n = int(raw_input())
        dp = [0 for x in xrange(n+1)]
        dp[0] = 1
        for i in xrange(1,n+1):
            for coin in coin_values:
                if i >= coin:
                    dp[i] += dp[i-coin]
        print dp[n]
    except(EOFError):
        exit()
