"""
reddit.com/r/dailyprogrammer challenge #214-Easy, posted at: http://redd.it/35s2ds

Finding the standard deviation of a set of numbers

Input

The input will consist of a single line of numbers separated by spaces. The numbers will all be positive integers.
Output

Your output should consist of a single line with the standard deviation rounded off to at most 4 digits after the decimal point.
"""

def easy214(inString):
    nums=[int(x) for x in inString.split()]
    mean=sum(nums)/float(len(nums))

    dev=0
    for num in nums:
        dev+=(num-mean)**2
    return round((dev/float(len(nums)))**0.5,4)
