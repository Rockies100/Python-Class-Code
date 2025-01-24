#This program is titled 'Camping List'. It shows the ability to use functions that manipulate a list.
#Gavin Van Horn
#January 23rd, 2025

#Step 1
camping_equip = ['tent', 'grill', 'fishing Pole', 'cooler', 'propane', 
                'boots', 'kayak', 'chairs', 'lighter', 'corn hole']
camping_equip.sort()
print(len(camping_equip))
print(camping_equip)

#Step 2
camping_equip.append('matches')
print(camping_equip)

#Step 3
camping_equip[6] = 'binoculars'
print(camping_equip)

#Step 4
camping_equip.remove('binoculars')
print(camping_equip)