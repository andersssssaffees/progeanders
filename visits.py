from pprint import pprint

file = open('visits.csv', encoding='utf-8')


visits = {}
for row in file:
    pair = row.strip('\ufeff').split(';')
    visits[pair[0].strip()] = int(pair[1].strip())

max = 0
max_key = ''

for visit in visits:
    if visits[visit] > max:
        max_key = visit
        max = visits[visit]

# pprint(visits)

print('Kõige rohkem külastusi oli ' + max_key + ', siis külastus parki ' + str(visits[max_key]) + ' inimest')