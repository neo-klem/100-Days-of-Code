print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))
tip_percent = int(input("How much tip would you like to give? 10,12 or 15? "))
number_of_people = int(input("How many people to split the bill? "))

each_persons_part = (total_bill + (total_bill * (0.01 * tip_percent))) / number_of_people

print(f"Each person should pay: ${each_persons_part:.2f}")