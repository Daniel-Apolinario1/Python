# ---------------------------------------------------------------
#           %%%%%      DAY TWO PROJECT      %%%%%
# ---------------------------------------------------------------
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people_to_split = int(input("How many people to split the bill? "))

tip = bill * tip_percentage/100

amount_to_pay = (bill + tip)/people_to_split

print(f"Each person should pay: ${amount_to_pay: .2f}")
