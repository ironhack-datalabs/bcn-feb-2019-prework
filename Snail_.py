'''A snail falls at the bottom of a '125' cm well.
Each day the snail rises 30 cm.
But at night, while sleeping, slides 20 cm because the walls are wet.
How many days does it take for the snail to escape the well?
Hint: The snail gets out of the well when it surpasses the 125cm of height.
'''


'''
Loop: while
Conditional statements: if-else
Function: print()
'''

'''1. Assign the challenge data to variables with representative names: 
well_height, 
daily_distance, 
nightly_distance and snail_position.'''


advance_cm = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]
well_height = 125
daily_distance = 30
nightly_distance = 20
snail_position = 0
notEscaped = True

# Create a variable days to keep
#count of the days that pass until the snail escapes the well

days = 0

fullDaylydist = daily_distance - nightly_distance

while snail_position < well_height:
    print(str(days) + " day gone")
    snail_position += fullDaylydist
    if snail_position < well_height:
        days += 1
# Print the solution.
else: print(str(days) + "days and I am out from the well!")  #"odaertunk +" str(days) " nap alatt")



'''Bonus
The distance traveled by the snail each day is now defined by a list.
advance_cm = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]
On the first day, the snail rises 30cm but during the night it slides 20cm. On the second day, the snail rises 2
1cm but during the night it slides 20cm, and so on.'''


#How many days does it take for the snail to escape the well?
#Follow the same guidelines as in the previous challenge.
#Hint: Remember that the snail gets out of the well when it surpasses the 125cm of height.