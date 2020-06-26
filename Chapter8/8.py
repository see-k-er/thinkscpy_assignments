<<<<<<< HEAD
#to convert a given image into grayscale

import image

img_lu = image.Image("luther.jpg")
win = image.ImageWin(img_lu.getWidth(),img_lu.getHeight())
img_lu.draw(win)
img_lu.setDelay(0)

def grayscale(img):
    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            pix = img.getPixel(col,row)

            grayscale = (pix.getRed()+pix.getGreen()+pix.getBlue()) / 3

            newImage = image.Pixel(grayscale,grayscale,grayscale)

            img.setPixel(col,row,newImage)


grayscale(img_lu)
print("Converted")
win.exitonclick()
