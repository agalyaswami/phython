denominations = [1, 2, 5, 10, 20, 50, 100, 200, 500]

amount = 1900

for denom in sorted(denominations, reverse=True):
    if amount >= denom:
        print(amount//denom, ' notes of ', denom)
        amount = amount%denom
if amount==0:
    break
