name = input('Sisesta toote nimi: ')

product = ''   
price = 0.0

if name.lower() == 'maasikas':
    product = 'maasikas'
    price = 5
if name.lower() == 'vaarikas':
    product = 'vaarikas'
    price = 5.2

else:
    product = 'tundmatu'

print(product.capitalize() + ' maksab ' + str(price) + ' eurot' if product != 'tundmatu' else 'Meil ei ole sellist toodet')
