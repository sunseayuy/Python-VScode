price_house = 10000
buyer_credit = False
if buyer_credit:
    price_house *= 0.1
else :
    price_house *= 0.2
print(f'Price: ${price_house}')
