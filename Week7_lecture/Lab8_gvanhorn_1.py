#This program is titled, 'UPC Check Number'. The code will take the UPC input from the user
#and calculate the check number for that associated UPC code.
#Gavin Van Horn
#March 1st, 2025

def find_upc():
    upc = str(input('Enter the 12 digit UPC code with *NO* spaces: '))
    
    if len(upc) != 12:
        print('That is an invalid input. Please try again.')
        return find_upc()
    else:
        odd_digits = upc[0:11:2]
        even_digits = upc[1:11:2]

        odd_sum = sum(map(int,odd_digits)) * 3

        total_sum = odd_sum + sum(map(int,even_digits))

        mod_ten = total_sum % 10

        if mod_ten == 0:
            check_digit = mod_ten
            print(f"The check digit for this UPC code is {check_digit}")
        else:
            check_digit = 10 - mod_ten
            print(f"The check digit for this UPC code is {check_digit}.")
find_upc()