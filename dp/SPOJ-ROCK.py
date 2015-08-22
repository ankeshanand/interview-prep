def compute_zero_counts(rock_desc):
    zero_counts = [0 for i in xrange(N+1)]
    for i in xrange(1, N+1):
        zero_counts[i] = zero_counts[i-1]
        if rock_desc[i-1] == '0':
            zero_counts[i] += 1

    return zero_counts

def score(zero_counts, start, end):
    length = end - start + 1
    zeroes = zero_counts[end] - zero_counts[start-1]
    ones = length - zeroes
    if ones > zeroes:
        return length
    return 0

t = int(raw_input())
for case in xrange(t):
    N = int(raw_input())
    rock_desc = raw_input()

    zero_counts = compute_zero_counts(rock_desc)
    dp = [0 for i in xrange(N+1)]

    for i in xrange(1,N+1):
        for j in xrange(0,i):
            dp[i] = max(dp[i], dp[j] + score(zero_counts, j+1, i))

    print dp[N]




