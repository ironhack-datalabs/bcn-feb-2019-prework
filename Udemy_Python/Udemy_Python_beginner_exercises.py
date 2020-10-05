'''
A customer of a grocery store is purchasing 6 items. The names and prices of the items are as follows:
Penne 16 oz Pack of 12 - $16.68
Arrabiata Pasta Sauce 24 oz - $6.98
Bag of 20 Organic Garlic Cloves - $16.78
Italian Seasoning 1.5 oz Bottle - $15.26
Artisan Baguettes Twin Pack - $3.00
12 oz Bag of Meatballs - $4.39
In a .py file, write a program which calculates the subtotal of all 6 of these items using an expression.
The subtotal is just the sum of all of their prices.
Use print() to display the result of the expression.



Penne_16oz_Pack_of_12 = 16.68 * 100
Arrabiata_Pasta_Sauce_24oz = 6.98 * 100
Bag_of_20_Organic_Garlic_Cloves = 16.78 * 100
Italian_Seasoning_1_5oz_Bottle = 15.26 * 100
Artisan_Baguettes_Twin_Pack = 3.00 * 100
_12_oz_Bag_of_Meatballs = 4.39 * 100
Grocery = [Penne_16oz_Pack_of_12,
Arrabiata_Pasta_Sauce_24oz,
Bag_of_20_Organic_Garlic_Cloves,
Italian_Seasoning_1_5oz_Bottle,
Artisan_Baguettes_Twin_Pack,
_12_oz_Bag_of_Meatballs]

_sum = sum(Grocery)/100
print(_sum)

#
#

a = "Just do it!"  # Create a variable and assign it the string "Just do it!"
print(a[10])  # Access the "!" from the variable by index and print() it
print(a[5:7])  # Print the slice "do" from the variable
print(a[8:])  # Get and print the slice "it!" from the variable
print(a[:5])  # Print the slice "Just" from the variable
print(a[5:])  # Get the string slice "do it!"
print("Don't " + a.lower())
# from the variable and concatenate it with the string "Don't ".  Print the resulting string.

#
#

a = 1.23  # Create a variable and assign it a float
print(type(a))  # Use print() and type() to print the data type of the variable in the output
a = str(a)  # Use str() on the variable from step 1 and concatenate it with the string " is a float."
print(type(a))  #  then use print() to display the result
print(str("Hello, I'm Oliver,\nit's nice to meet you!"))
# print() the string "Hello, I'm [name], it's nice to meet you!"
(you will need to use the \' escape sequence.)

#
#


Using your knowledge of escape sequences, 
create a single print() statement with single string inside of it that displays this when the program is run:

print(str('*******\n ***** \n  ***  \n   *   '))

#
#

create a program and use input() three times to get answers to the following questions from a user.  
Store each of the answers in a variable.
What is your name?
What is your quest?
What is your favorite color?
Then, concatenate everything into a string within a print() statement 
with the form 'So your name is [name], your quest is [quest], and your favorite color is [color].'

name = input('What is your name?')  # name input
quest = input('What is your quest?')  # quest input
color = input('What is your favorite color?') # color input
print('So your name is ' + name +', your quest is ' + quest + ',and your favorite color is ' + color +'.')

#
#

In a Python file, use input() to ask the user to enter an integer that 10 will be added to.  
Assign what they type to a variable.
print() the sum of the integer they entered and 10.

a = int(input('enter an integer: '))
a += 10
print(a)

#
#

Create a function called hello_world_printer() which takes no parameters and prints the string "hello world"
Call the function hello_world_printer()

def hello_world_printer(a="hello world"):
    print(a)
hello_world_printer()

#
#

Create a function called name_printer which takes 1 parameter and prints it
Create a variable called name and assign it user input().  input()'s message should ask the user to enter their name.
Call name_printer() with the variable "name" as its argument.

def name_printer(a):
    print(a)


name = input('Enter your name: ')
name_printer(name)

#
#

For this programming challenge,
you will be creating a function that calculates the volume of a rectangular prism in feet.
The formula to find the volume of a rectangular prism is V = l * w * h 
where l, w, and h are length, width, and height, respectively.

First, create three variables representing length, width, and height.   
Assign each of them an integer as user input using the input() function and int().
Next, create a function to calculate the volume of the rectangular prism.  
It should have 3 parameters representing length, width, and height 
and return the volume of a rectangular prism calculated using those 3 parameters.
Finally, use print() 
to display "The volume of the rectangular prism is [call function  here to calculate volume] cubic feet." in the output.  
You will have to use str() on the function call to be able to concatenate it with strings since it returns an integer.


length = int(input('Enter the length of the prism: '))  # length input
width = int(input('Enter the length of the prism: '))  # width input
height = int(input('Enter the height of the prism: '))  # height input


def volume(a, b, c):
    return a * b * c
print("The volume of the rectangular prism is " + str(volume(length, width, height)) + " cubic feet. ")


#
#


The formula for converting from degrees Celsius to degrees Fahrenheit is as follows:
F = 1.8 * C + 32
Where F is the Fahrenheit temperature and C is the Celsius temperature.

create a variable and assign it an integer representing a celsius temperature that is entered as user input().  
input()'s message should prompt the user to enter an integer value.

For this programming challenge, you will 
then write a function called fahrenheit that takes in an integer representing a Celsius temperature as its argument.  
The function will return the Fahrenheit equivalent temperature of that argument to 1 place after the decimal.

At the end of your program, 
display the Fahrenheit equivalent in a print statement message formatted like so:  
"The Fahrenheit equivalent of [user entered integer] degrees Celsius is [number returned by function]".
To make sure that the function works, 
run your program multiple times
and call the function on different user entered integer values both negative and positive.


cTemp = int(input('Enter the Celsius temperature as integer: '))


def fahrenheit(a):
    return round((1.8 * a + 32), 1)


print("The Fahrenheit equivalent of " + str(cTemp) + " degrees Celsius is " + str(fahrenheit(cTemp)) + ".")


#
#

'''