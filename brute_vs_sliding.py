# Brute force solution: O(nk) time
def best_total_price(prices, k):
    maxtotal = 0
    for i in range(len(prices)-k+1):
        total = sum(prices[i:i+k])
        maxtotal = max(maxtotal, total)
    return maxtotal

  
# Sliding window solution: O(n) time
def best_total_price(prices, k):
    if len(prices) < k:
        return 0
    total = sum(prices[:k])
    maxtotal = total
    for i in range(len(prices)-k):
        total -= prices[i]
        total += prices[i+k]
        maxtotal = max(maxtotal, total)
    return maxtotal
