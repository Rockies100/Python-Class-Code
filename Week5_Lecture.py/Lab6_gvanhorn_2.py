#This program is titled 'Largest Rivers' and contains a dictionary of 
# the three largest rivers and the country of the river
#Gavin Van Horn
#February 19th, 2025

rivers = {
    'Nile': 'Egypt',
    'Amazon': 'Brazil',
    'Yangtze': 'China'
} 

for river, country in rivers.items():
    print(f"The {river} runs through {country}.")
print()
print('The following Rivers are in the dictionary:')
for river in rivers:
    print(river)
print()
print('The following Countries are in the dictionary:')
for country in rivers:
    print(rivers[country])