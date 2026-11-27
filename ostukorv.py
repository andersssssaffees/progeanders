ostukorv = []

while True:
    toode = input("Lisa toode ostukorvi (toote nimi) või vaata sisestatuid tooteid ('q'): ")
    if toode.lower() == "q":
        break
    ostukorv.append(toode)

ostukorv.sort()
print(f"Ostukorvis on {len(ostukorv)} toodet:")

indeks = 0
while indeks < len(ostukorv):
    print(ostukorv[indeks].capitalize())
    indeks += 1
