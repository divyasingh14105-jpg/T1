T1

# Electricity Bill Calculator
# Write a program that calculates the electricity bill based on units consumed using different rates for different slabs.

# 100 and below = 3
# 100-200 = 5
# 200-300 = 7
# 300 above = 10


# Taking units consumed as input
units = int(input("Enter Units Consumed: “))

# Calculating bill based on slabs
if units <= 100:
    totalBill = units * 3

elif units <= 200:
    totalBill = (100 * 3) + ((units - 100) * 5)

elif units <= 300:
    totalBill = (100 * 3) + (100 * 5) + ((units - 200) * 7)

else:
    totalBill = (100 * 3) + (100 * 5) + (100 * 7) + ((units - 300) * 10)

# Displaying the final bill
print(f"Total Electricity Bill: ₹{totalBill}")


# Student Marks Analyzer
# Write a program that accepts the marks obtained by a student in five subjects.
# The program should determine the highest marks, lowest marks, and average marks obtained by the student, and display all three results.

# Variables to Store Highest, Lowest and Average Marks
highestMarks = 100
lowestMarks = 0


# Taking Marks for Five Subjects as Input
subject1 = int(input("Enter Marks for Subject 1: "))
subject2 = int(input("Enter Marks for Subject 2: "))
subject3 = int(input("Enter Marks for Subject 3: "))
subject4 = int(input("Enter Marks for Subject 4: "))
subject5 = int(input("Enter Marks for Subject 5: "))



# Finding the Highest Marks
if highestMarks < subject1:
    highestMarks =  subject1

elif highestMarks < subject2:
    highestMarks =  subject2

elif highestMarks < subject3:
    highestMarks =  subject3

elif highestMarks < subject4:
    highestMarks = subject4

elif highestMarks < subject5:
    highestMarks = subject5




# Finding the Lowest Marks
if lowestMarks > subject1:
    lowestMarks = subject1

elif lowestMarks > subject2:
    lowestMarks = subject2

elif lowestMarks > subject3:
    lowestMarks = subject3

elif lowestMarks > subject4:
    lowestMarks = subject4

elif lowestMarks > subject5:
    lowestMarks = subject5



# Calculating the Average Marks
avg = subject1 + subject2 + subject3 + subject4 + subject5 / 5

# Displaying the Results
print(f"Highest: {highestMarks}")
print(f"Lowest: {lowestMarks}")
print(f"Average: {avg}")


# Shopping Cart Total
# Write a program that calculates the total price of a product based on the product selected and the quantity entered by the user. The program should support the 
# four available products and display the total amount that needs to be paid


# Product prices
headPhone = 999
smartWatch = 1599
PS5 = 1299
iPad = 599

# Taking input from the user
productName = input("Enter Product Name: ")
quantity = int(input("Enter the Quantity of the Product: "))

# Calculating total price
if productName == "headPhone":
    totalPrice = headPhone * quantity

elif productName == "smartWatch":
    totalPrice = smartWatch * quantity

elif productName == "PS5":
    totalPrice = PS5 * quantity

elif productName == "iPad":
    totalPrice = iPad * quantity

else:
    totalPrice = 0
    print("Invalid Product Name!")
    
# Displaying the total amount
if totalPrice > 0:
    print(f"Total Amount To Be Paid: ₹{totalPrice}")



# Password Validator
# Write a Python program that validates a user's password.

# A password is considered valid if:
# It contains at least 8 characters
# It contains at least one uppercase letter
# It contains at least one lowercase letter
# It contains at least one digit

# The program should display whether the password is valid or invalid.

password = input("Enter password: ")

has_upper = False
has_lower = False
has_digit = False

if len(password) >= 8:
    for char in password:
        if char.isupper():
            has_upper = True

        if char.islower():
            has_lower = True

        if char.isdigit():
            has_digit = True

    if has_upper and has_lower and has_digit:
        print("Valid Password")
    else:
        print("Invalid Password")
else:
    print("Invalid Password")








