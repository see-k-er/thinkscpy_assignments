#to remove the red from an image. To make the red pixel value to zero.
import image

img = image.Image("luther.jpg")
win = image.ImageWin(img.getWidth(), img.getHeight()) #to get the image in a separate window
img.draw(win)
img.setDelay(0)

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        pix = img.getPixel(col,row)
        
        newRed = 0 #removing red component     
        newpix = image.Pixel(newRed, pix.getGreen(),pix.getBlue())
        
        img.setPixel(col,row,newpix)
        
win.exitonclick()