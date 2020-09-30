weight = input('Weight: ')
weight_number=int(weight)
chouse = input('(L)bs or (K)g: ')
if chouse.upper() == 'L':
    print(f'You are {0.45*weight_number} kilos.')
elif chouse.upper() == 'K' :
    print(f'You are {weight_number/0.45} pounds.')