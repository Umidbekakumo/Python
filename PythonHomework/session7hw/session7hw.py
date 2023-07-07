
Kumo = {"salary": 15000, "age": 23, "car, laptop, tv, and monitor": 1}
mike = {"salary": 10000, "age": 20, "car, PC, smartwatch, and boat": 1}
 
lst2 = [num for num in range(51)]
lst_even = sum([num for num in lst2 if num % 2 == 0])
#print("some of all even numbers is ", lst_even)

odd_prod = 1
for num in lst2:
    if num % 2 == 1:
        odd_prod *= num
        #print('product of all odd numbers is', odd_prod)

largest_num = max(lst2)

print('Sum of even numbers :', lst_even)
print('Product of odd numbers :', odd_prod)
print('Largest number:', largest_num)

