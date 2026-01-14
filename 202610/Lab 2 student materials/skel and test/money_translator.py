# Author: Caroline Hardin
# Date: 1/13/2026
# Solution code for money translator 

from format_as_money import format_as_dollars

donors_name = input("The name of the person making the donation: ")
print(donors_name, end = "")

their_money = float(input("'s net worth in millions: "))
#print(donors_name, end = " ")
their_money_actual = their_money * 1000000 #times a million
their_money_net = their_money_actual - 13590 #subtract federal Poverty Level

#print(format_as_dollars(their_money_actual), " is ", donors_name, "'s actual money")
#print("$", '{0:,.2f}'.format(their_money_actual) , " is ", donors_name, "'s actual money")

#f'{their_money_actual:.2f}'
donation = int(input("Enter the amount of the donation: "))


your_money = float(input("Your (or ordinary person's) net worth: "))
your_money_net = your_money - 13590
scaled_donation = (donation/their_money_net* your_money_net)

#print("$",'{0:,.2f}'.format(donation), "donation for someone with a net worth of $",'{0:,.2f}'.format(their_money_actual) ,"is the same as a $",'{0:,.4f}'.format(scaled_donation), "donation for someone with a net worth of $",'{0:,.2f}'.format(your_money) )
print(format_as_dollars(donation), "donation for someone with a net worth of", format_as_dollars(their_money_actual) ,"is the same as a",format_as_dollars(scaled_donation), "donation for someone with a net worth of", format_as_dollars(your_money))