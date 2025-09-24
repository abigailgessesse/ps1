from math import pi

"""
There is lots you can do with Python's math module!
Here we are going to practice using some of the functions given to us.
"""

# Question 2B (continued from written portion)

def run_total_seconds(easy_miles, tempo_miles):
    """
    Return the total seconds of a run with `easy_miles` miles at an easy pace
    and `tempo_miles` miles at a tempo pace.
    """
    # A runner runs easy_miles at an easy pace (8:15 per mile)
    # and tempo_miles miles at tempo pace (7:12 per mile). 
    # TODO: Write a function to calculate the total time of the run in seconds.

    easy_seconds = easy_miles * 495
    # easy: 8*60 + 15 = 495 seconds = 1 easy mile
    tempo_seconds = tempo_miles * 432
    # tempo: 7*60 + 12 = 432 seconds = 1 tempo mile
    totalTime = easy_seconds + tempo_seconds
    return totalTime

print(run_total_seconds(1,1))