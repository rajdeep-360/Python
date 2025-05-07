
###Assignment_2

#Task 1
num1 = int(input("Enter a number: "))
if num1 % 2 == 0:
    print(num1, "is an even number")
else:
    print(num1, "is an odd number")


#Task 2
sum1 = 0
for i in range(1, 51):
    sum1 += i
print("The sum of numbers from 1 to 50 is:", sum1)
