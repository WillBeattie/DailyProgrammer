"""
reddit.com/r/dailyprogrammer challenge #214-Intermediate, posted at: http://redd.it/35s2ds
Description

Have you ever layered colored sticky notes in interesting patterns in order to make pictures? You can create surprisingly complex pictures you can make out of square/rectangular pieces of paper. An interesting question about these pictures, though, is: what area of each color is actually showing? We will simulate this situation and answer that question.
Start with a sheet of the base color 0 (colors are represented by single integers) of some specified size. Let's suppose we have a sheet of size 20x10, of color 0. This will serve as our "canvas", and first input:
20 10
We then place other colored sheets on top of it by specifying their color (as an integer), the (x, y) coordinates of their top left corner, and their width/height measurements. For simplicity's sake, all sheets are oriented in the same orthogonal manner (none of them are tilted). Some example input:
1 5 5 10 3
2 0 0 7 7 
This is interpreted as:
Sheet of color 1 with top left corner at (5, 5), with a width of 10 and height of 3.
Sheet of color 2 with top left corner at (0,0), with a width of 7 and height of 7.
Note that multiple sheets may have the same color. Color is not unique per sheet.
Placing the first sheet would result in a canvas that looks like this:
00000000000000000000
00000000000000000000
00000000000000000000
00000000000000000000
00000000000000000000
00000111111111100000
00000111111111100000
00000111111111100000
00000000000000000000
00000000000000000000
Layering the second one on top would look like this:
22222220000000000000
22222220000000000000
22222220000000000000
22222220000000000000
22222220000000000000
22222221111111100000
22222221111111100000
00000111111111100000
00000000000000000000
00000000000000000000
This is the end of the input. The output should answer a single question: What area of each color is visible after all the sheets have been layered, in order? It should be formatted as an one-per-line list of colors mapped to their visible areas. In our example, this would be:
0 125
1 26
2 49
Sample Input:

20 10
1 5 5 10 3
2 0 0 7 7
Sample Output:

0 125
1 26
2 49
"""


def medium214():
    print "Enter data"
    inData = list(iter(raw_input, ""))
    print "------------------\n"

    dims=[int(x) for x in inData[0].split()]
    cards=[]
    for line in inData[1:]:
        cards.append([int(x) for x in line.split()])
        
    Image=[[0 for x in range(dims[0])] for x in range(dims[1])]    
    
    for x in range(dims[0]):
        for y in range(dims[1]):
            for card in cards:
                if fallsIn([x,y],card):
                    Image[y][x]=card[0]
    for line in Image:
        print line

    #Generate a list of n zeros where n is the number of colours
    count=[0]
    for card in cards:
        count.append(0)

    for line in Image:
        for item in line:
            count[item]+=1 #This assumes the colors are numbered sequentially

    return count

def fallsIn(loc,card):
    #Determine if a coordinate falls in the rectangle bounded by a card
    if loc[0]>=card[1] and loc[0]<card[1]+card[3]:
        if loc[1]>=card[2] and loc[1]<card[2]+card[4]:
            return True
    return False
