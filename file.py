file = open('visits.csv', encoding='UTF-8')

for row in file:
    for element in row:
        print(element)

file.close()