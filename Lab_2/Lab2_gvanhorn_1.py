#The name of this program is "Suggested Tip". It takes an input of the bill total from the user, and outputs a suggested 15% and 20% tip. It will take another user input on the selection, and output the total with tip included.
#Author: Gavin Van Horn
#Date: January 21st, 2025

bill_total = float(input("Enter bill total:"))

tip_15 = bill_total * 0.15
tip_20 = bill_total * 0.2

print(f"A 15% tip would be ${tip_15:.2f}. A 20% tip would be ${tip_20:.2f}.")

def tip_select(): 
    tip_choice = input(f"Enter 15 or 20 to get your total with tip: ")
    if tip_choice == '15' :
        bill_tip_15 =  bill_total + tip_15
        return print(f"Your total is ${bill_tip_15:.2f} with a 15% tip. Thank you!")
    elif tip_choice == '20':
        bill_tip_20 = bill_total + tip_20
        return print(f"Your total is ${bill_tip_20:.2f} with a 20% tip. Thank you!")
    else:
        print('You must select 15 or 20.')
        return tip_select()
tip_select()