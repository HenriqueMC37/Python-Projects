import math
#input type of calculator user wants to use
type_of_calculation = input('''investment - to calculate the amount of interest you'll earn on your investment \n
bond - to calculate the amount you'll have to pay on a home loan \n 
Enter either 'investment' or 'bond' from the menu above to proceed: ''').lower()

#elif statement to select type of calculator
if type_of_calculation == "investment":

    rate = (float(input("Please enter the interest rate: ")) / 100)
    
    principal_amount = float(input("Please enter how much money you want to deposit: "))
    
    time = float(input("Please enter how many years you are planning on investing for: "))
    
    interest = input("Would you prefer 'simple' or 'compound' interest?").lower()

    #if-elif-else statement to calculate different types of interest on investment   
    if interest == "simple":

        accumulated_amount = principal_amount*(1 + rate*time)
        #decided to also create a variable for profit, so it will be easier for the user to figure out how much they will make out of the investment
        profit = accumulated_amount - principal_amount

        print(f'''After {str(time)} years, your profit will be {str(profit)}, bringing your accumulated amount to a total of {str(accumulated_amount)}.''')

    elif interest == "compound":

        accumulated_amount = principal_amount * math.pow((1 + rate), time)

        profit = accumulated_amount - principal_amount

        print(f'''After {str(time)} years, your profit will be {str(profit)}, bringing your accumulated amount to a total of {str(accumulated_amount)}.''')

    else:
        print("Error: You did not enter either 'simple' nor 'compound'. Please restart the process.")

elif type_of_calculation == "bond":

    house_value = float(input("Please enter the value of the house: "))

    monthly_interest_rate = (((float(input("Please enter the interest rate: "))) /100) / 12)

    number_of_months = float(input("Please input the number of months over which the bond will be repaid: "))

    repayment = (monthly_interest_rate * house_value) / (1 - (1 + monthly_interest_rate)**(-number_of_months))

    print(f"You will have to repay {str(repayment)} per month for {str(number_of_months)} months.")

else:
    print("Error: Please enter either 'investment' or 'bond'.")

'''I know I did not keep the lines of code within the 72 lines, but I 
attempted to use backlash among other ways to keep the lines shorter
but for some reason it did not work when it came to the strings on 
lines 25 and 33. That being the case, I left the rest in single lines
as well to keep the code uniform. '''
