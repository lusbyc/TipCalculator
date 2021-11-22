print("Exercise 3: Tip Calculator")

totalBill = float(input("What's the total amount of the bill? "))
num_of_people = int(input("How many people were there? "))
total_per_person = format(totalBill / num_of_people,".2f")
print(f"The total per person is ${total_per_person}.")
