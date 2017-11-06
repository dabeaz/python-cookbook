# example.py
#
# Example of calculating with dictionaries
from operator import itemgetter

prices = {
   'ACME': 45.23,
   'AAPL': 612.78,
   'IBM': 205.55,
   'HPQ': 37.20,
   'FB': 10.75
}

# Find min and max price
min_price = min(prices.items(), key=itemgetter(1))
max_price = max(prices.items(), key=itemgetter(1))

print('min price:', min_price)
print('max price:', max_price)

print('sorted prices:')
prices_sorted = sorted(prices.items(), key=itemgetter(1))
for name, price in prices_sorted:
    print('    ', name, price)


