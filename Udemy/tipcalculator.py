print('Welcome to the Tip Calculator! ')
total = input('How much was the total bill? $')
total2 = float(total)
tip1 = int(input('What percentage would you like to tip 10, 12, 15? '))
people = int(input( "how many people will split the bill? "))
tip_percent = tip1 / 100 
tip_total = total2 + tip_percent
total_bill = total2 + tip_total
person_per_bill = total_bill / people 
final_bill = round(person_per_bill, 2)
print(f'Each person should pay ${final_bill} ')
