# Author:
# Date:
# Description:

#be sure format_as_money.py is in the same folder
from format_as_money import format_as_dollars

#2026 numbers
fed_poverty_level = 15650

#A. get the name of the person who donated
donation = 0
#"The name of the person making the donation: "

#B get input from the user, save as a float. Use the persons name in the request
their_money_actual = 0
#"'s net worth in millions: "

#C get the amount of the donation. Save as a float
#"Enter the amount of the donation: "

#D get the net worth of the user. Save as a float
your_money = 0
#"Your (or ordinary person's) net worth: ")

#D calculate what the equivalent donation would be for a person of average net worth.
# First figure out what percent of the donator's money (minus federal poverty level) the donation is, then
# multiply that by the average persons net worth (minus federal poverty level)
scaled_donation = 0

# Below is the final output for the user. You don't need to change anything as long as the variable names are the same
print(format_as_dollars(donation), "donation for someone with a net worth of", format_as_dollars(their_money_actual) ,"is the same as a",format_as_dollars(scaled_donation), "donation for someone with a net worth of", format_as_dollars(your_money))

