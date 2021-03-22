print("Welcome to the tip calculator")
total_bill = float(input("What is the total bill? $"))
people = int(input("How many people to split the bill? "))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15 "))
per_person = total_bill / people
percent = (per_person * percentage) / 100
solution = per_person + percent
print(f"Each person should pay {solution:.1f}")