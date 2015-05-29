"""
reddit.com/r/dailyprogrammer challenge #210-Intermediate, posted at: http://redd.it/35s2ds

Drawing a Gradient

Description

One of the most basic tools in graphic design toolbox is the "gradient": a smooth transtion from one color to another. They are remarkably useful and are available in virtually every graphic design program and graphic programming library, and even natively in design languages like CSS and SVG.
Your task today is to make a program that can generate these wonderful gradients, and then either draw it to the screen or save it as an image file. You will get as inputs pixel dimensions for the size of the gradient, and the two colors that the gradient should transition between.
NOTE: As I said, there are many imaging libraries that provide this functionality for you, usually in some function called drawGradient() or something similar. You are strongly encouraged not to use functions like this, the spirit of this challenge is that you should figure out how to calculate the gradient (and thus the individual pixel colors) yourself.
This isn't an ironclad rule, and if you really can't think of any way to do this yourself, then it's fine to submit your solution using one of these functions. I encourage you to try, though.
It is, however, perfectly acceptable to use a library to save your pixels in whatever format you like.
Formal Inputs & Outputs

Input description

Your input will consist of three lines. The first line contains two numbers which is the width and the height of the resulting gradient. The other two lines consist of three numbers between 0 and 255 representing the colors that the gradient should transition between. The first color should be on the left edge of the image, the second color should be on the right edge of the image.
So, for instance, the input
500 100 
255 255 0 
0 0 255
means that you should draw a 500x100 gradient that transitions from yellow on the left side to blue on the right side.
Output description

You can either choose to draw your gradient to the screen or save it as an image file. You can choose whatever image format you want, though it should preferably a lossless format like PNG.
"""

from PIL import Image
def medium210(width=1000,height=100,c2=[204,119,34],c1=[1,66,37]):

    im=Image.new("RGB",(width,height),"white")    
    
    for w in range(width):
        for h in range(height):
            px=[]
            for i in range(3):
                px.append((w*c1[i]+(width-w)*c2[i])/width)
            im.putpixel((w,h),tuple(px))
    im.save("C:/Users/Will/Desktop/test.jpg")
