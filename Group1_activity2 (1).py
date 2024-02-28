"""
Done by: Group 1
Title: Activity 2 - currency converter program

Done by:
Al Tajer, Bachar 
Faizah Mehek
micheal

GitHub_URL: https://github.com/54izah/group1_activity1.git
            https://github.com/Ba7992/GCIS-123.git


CONTRIBUTION:
Bachar - def main():
Faizah - def aed_to_eur(money): - def aed_to_britishPound(money): - def aed_to_dollar(money): 
micheal - def dollar_to_aed(amount): - def britishPound_to_aed(amount): - def eur_to_aed(amount):


This program uses to develop a simple currency converter program in Python. The
program should allow users to convert currency values between United Arab Emirates Dirham
(AED), Euro (EUR), British Pound (GBP), and US Dollar (USD). 

Functions:
def aed_to_eur(money):  Conversion rate from AED to Euro
def aed_to_britishPound(money): Conversion rate from AED to British Pound
def aed_to_dollar(money): Conversion rate from AED to US Dollar
def dollar_to_aed(amount): Conversion rate from US Dollar to AED
def britishPound_to_aed(amount): Conversion rate from British Pound to AED
def eur_to_aed(amount): Conversion rate from Euro to AED
def main():Main function to execute the currency converter
"""

AED_TO_EUR=0.25 # Conversion rate from AED to Euro
AED_TO_BRITISHPOUND=0.21 # Conversion rate from AED to British Pound
AED_TO_DOLLAR=0.27 # Conversion rate from AED to US Dollar

DOLLAR_TO_AED=3.67 # Conversion rate from US Dollar to AED
BRITISHPOUND_TO_AED=4.66 # Conversion rate from British Pound to AED
EUR_TO_AED=3.98 # Conversion rate from Euro to AED

#Converts money from AED to Euro
def aed_to_eur(money):
    return money*AED_TO_EUR

#Converts money from AED to British Pound
def aed_to_britishPound(money):
    return money*AED_TO_BRITISHPOUND

#Converts money from AED to US Dollar
def aed_to_dollar(money):
    return money*AED_TO_DOLLAR

#Converts amount from US Dollar to AED.
def dollar_to_aed(amount):
    return amount*DOLLAR_TO_AED

#Converts amount from British Pound to AED
def britishPound_to_aed(amount):
    return amount*BRITISHPOUND_TO_AED

#Converts amount from Euro to AED
def eur_to_aed(amount):
    return amount*EUR_TO_AED

# Main function to execute the currency converter
def main():
    while True:
        token="     \" Main Menu \"_Welcome to Currency Converter  "
        tokens=token.split("_")
        for i in tokens:
            print(i)
        print("---------------------------------")
        print("Select the conversion direction:")
        token="1. AED to other currencies_2. Other currencies to AED_3. Exit "
        tokens=token.split("_")
        for token in tokens:
            print(token)
        print()
        amount=float(input("put your amount of money you want to convert:"))
        your_choice=input("Enter your choice (1/2/3):")

        # AED to other currencies conversion
        if your_choice=="1":
            token="1. AED to Euro (EUR)_2. AED to British Pound (GBP)_3. AED to US Dollar_4. AED to Exit "
            tokens=token.split("_")
            for token in tokens:
                print(token)
            
            submit_your_choice=input("Enter the Sub choice of currency:")
            
            if submit_your_choice=="1":
                print(amount,"AED is equal to",aed_to_eur(amount),"EUR")
                user_input=input("Do you want to continue (y/n):")
                if user_input=="y":
                    continue
                if user_input=="n":
                    break

            if submit_your_choice=="2":
                print(amount,"AED is equal to",aed_to_britishPound(amount),"BRITISHPOUNT")
                user_input=input("Do you want to continue (y/n):")
                if user_input=="y":
                    continue
                if user_input=="n":
                    break

            if submit_your_choice=="3":
                print(amount,"AED is equal to",aed_to_dollar(amount),"DOLLAR")
                user_input=input("Do you want to continue (y/n):")
                if user_input=="y":
                    continue
                if user_input=="n":
                    break

            if submit_your_choice=="4":
                user_input=input("Do you want to continue (y/n):")
                if user_input=="y":
                    continue
                if user_input=="n":
                    break

                
        
        # Other currencies to AED conversion
        if your_choice=="2":
            token="1. Euro (EUR) to AED_2. British Pound (GBP) to AED_3. Dollar to AED_4. Exit"
            tokens=token.split("_")
            for token in tokens:
                print(token)
            submit_your_choice=input("Enter the Sub choice of currency:")
            
            if submit_your_choice=="1":
                print(amount,"EUR is equal to",eur_to_aed(amount),"AED")
                user_input=input("Do you want to continue (y/n):")
                if user_input=="y":
                    continue
                if user_input=="n":
                    break

            if submit_your_choice=="2":
                print(amount,"BRITISHPOUNT is equal to",britishPound_to_aed(amount),"AED")
                user_input=input("Do you want to continue (y/n):")
                if user_input=="y":
                    continue
                if user_input=="n":
                    break

            if submit_your_choice=="3":
                print(amount,"DOLLAR is equal to",britishPound_to_aed(amount),"AED")
                user_input=input("Do you want to continue (y/n):")
                if user_input=="y":
                    continue
                if user_input=="n":
                    break

            if submit_your_choice=="4":
                user_input=input("Do you want to continue (y/n):")
            if user_input=="y":
                continue
            if user_input=="n":
                break

         # Exit from the program
        if your_choice=="3":
            break

if __name__=="__main__":
    main()