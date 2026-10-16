length = float(input('Sisesta oma pikkus (cm): '))
weight = float(input('Sisesta oma kaal (kg): '))

bmi = round(weight / (length / 100) ** 2, 1)
print('Sinu kehamassiindeks on ' + str(bmi))