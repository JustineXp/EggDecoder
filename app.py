from countries import countries

eggcode = input('Enter the Egg Code : ')

farmingmethods = ['Organic', 'Free Range', 'Barn', 'Cage']
eggdetails = {'eggfm': '','country': '','farmid': ''}

countryabrev = eggcode[1:3]

eggdetails['eggfm'] = farmingmethods[int(eggcode[0])]
eggdetails['country'] = countries[countryabrev]
eggdetails['farmid'] = eggcode[3:]


print(f"Egg Code : {eggcode}")
print(f"{eggdetails['eggfm']} egg")
print(f"Country of Origin : {eggdetails['country']}")
print(f"Farm ID : {eggdetails['farmid']}")