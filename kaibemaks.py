inp = input('Sisesta toote hind koos käibemaksuga (eurodes): ')
price = float(inp)
outp = round(price / 1.24, 2)   
print('Toote hind ilma käibemaksuta on', outp, 'eurot')
