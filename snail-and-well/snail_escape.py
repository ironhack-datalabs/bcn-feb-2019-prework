"""
A snail falls at the bottom of a '125' cm well.
Each day the snail rises 30 cm.
But at night, while sleeping, slides 20 cm because the walls are wet.
How many days does it take for the snail to escape the well?
Hint: The snail gets out of the well when it surpasses the 125cm of height.
"""


'''
Loop: while
Conditional statements: if-else
Function: print()
'''

'''
 Assign the challenge data to variables with representative names: 
well_height, 
daily_distance, 
nightly_distance and snail_position.
'''
advance_cm = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]
'''
Bonus
The distance traveled by the snail each day is now defined by a list.
'''
well_height = 125
# daily_distance = 30
nightly_distance = 20
snail_position = 0
notEscaped = True


# Create a variable days to keep
# count of the days that pass until the snail escapes the well

days = 0

fullDaylydist = advance_cm[0] - nightly_distance

while snail_position < well_height:
    if days == 1:
        print(str(days) + " day gone")
    else:
        print(str(days) + " days gone")
    snail_position += advance_cm[days]
    if snail_position < well_height:
        snail_position -= nightly_distance  # The snail slides down the well here
        days += 1
# Print the solution.
    else:
        print(str(days) + " days and I am out from the well!")
        #  What is its maximum displacement in one day?
        print(str(max(advance_cm)) + " cm is the maximum distance the snail climbed in one day")
        #  And its minimum?
        #  Calculate the displacement using only the travel distance of the days used to get out of the well.
        print(str(min(advance_cm)) + " cm is the minimum distance the snail climbed in one day")
        # What is its average progress? Take into account the snail slides at night.
        # average_progress = (sum(days) * range(advance_cm)) - (sum(days) * nightly_distance)
        advSum = sum(advance_cm)
        advCnt = len(advance_cm)
        avgSpd = advSum / advCnt
        print(avgSpd)  # What is its average speed during the day?
        _stdDev = [(x - avgSpd) ** 2 for x in advance_cm]
        # What is the standard deviation of its displacement during the day?
        print(_stdDev)
