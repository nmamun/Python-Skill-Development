#!/usr/bin/env python

# ==============================================================
__author__ = "Nurul Mamun"
__date__ = " 13 July, 2020"
__version__ = "1.0"
__description__ = "Practice - Validating User Input"
# ==============================================================

# ========== Imports ===========================================

# ==============================================================

# ========= Functions ==========================================
def user_input():

    # Variable & initial values
    choice = 'wrong'
    acceptable_value = range(0,10)
    within_range = False

    # Conditions check
    while choice.isdigit() == False or within_range == False:
        choice = input("Please enter a number (0-10): ")

        # Digit check
        if choice.isdigit() == False:
            print("Sorry, that is not a digit")
        
        # Range check
        if choice.isdigit() == True:
            if int(choice) in acceptable_value:
                within_range = True
            else:
                print("Sorry, you are out of acceptable range (0-10)")
                within_range = False
    return int(choice)

# ==============================================================

# ========== Main Function =====================================
def main():
    user_input()



# ==============================================================


if __name__ == "__main__":
    main()