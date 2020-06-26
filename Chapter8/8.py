#to convet a given image into grayscale

import image

img = image.Image("luther.jpg")
win = image.ImageWin(img.getWidth(),img.getHeight())
img.draw(win)

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        pix = img.getPixel(col,row)
        
        grayscale = (pix.getRed()+pix.getGreen()+pix.getBlue()) / 3
        
        newImage = image.Pixel(grayscale,grayscale,grayscale)
        
        img.setPixel(col,row,newImage)
        
win.exitonclick()