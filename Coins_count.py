coins = list(map(int,input("Enter the denominations separated by spaces : ").strip().split()))
n = int(input("Enter the target amount: "))

i = 0
c = 0
coins.sort(reverse=True)
while n > 0 and i < len(coins):
    if n >= coins[i]:
        n -= coins[i]
        c += 1
    else:
        i+=1

print("Minimum number of coins needed are:", c, "remaining balance: $",n)