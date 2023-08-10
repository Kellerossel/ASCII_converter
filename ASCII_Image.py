from PIL import Image, ImageDraw, ImageFont
import math
from time import time

#You can change this if you want to:
fill_rgb = (0, 255, 0)
scaleFactor = 0.4
chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
#Please dont change this:
Charslist = list(chars)
charLength = len(Charslist)
interval = charLength/256
oneCharWidth = 10
oneCharHeight = 18

def printlogo():
    Logo = [   
"         _  __          ____                   _               _    _                            ",
"        | |/ /  ___    |  _ \  _ __  ___    __| | _   _   ___ | |_ (_)  ___   _ __   ___         ",
" _____  | ' /  / _ \   | |_) || '__// _ \  / _` || | | | / __|| _ || | / _ \ | '_ \ / __|  _____ ",
"|_____| | . \ | (_) |  |  __/ | |  | (_) || (_| || |_| || (__ | |_ | || (_) || | | |\__ \ |_____|",
"        |_|\_(_)___(_) |_|    |_|   \___/  \____| \____| \___| \__||_| \___/ |_| |_||___/        ",
"                                                                                                 ",
"                                                                                                 ",
"                      ---------- made by Kellerossel Productions ----------                      "
        ]
    for line in Logo:
        print( "\033[22m" + line)
printlogo()

def getCHAR(inputInt):
    return Charslist[math.floor(inputInt*interval)]
# This one text output of your image
with open("Output.txt","w") as text_file:
    text_file.write("")
text_file = open("Output.txt", "a")
# You must append your image to idle and write your image name down
try:
    im = Image.open(input("Image name: "))
except:
    print("[!] Cant open this Image")
    exit()
time1 = time()
font = ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf', 15)

width, height = im.size
im = im.resize((int(scaleFactor*width), int(scaleFactor*height*(oneCharWidth/oneCharHeight))), Image.NEAREST)
width, height = im.size
pixel = im.load()
# RGB = red green blue you can easily change color part between 0-255
outputImage = Image.new('RGB', (oneCharWidth * width, oneCharHeight * height), color = (0, 0, 0))
d = ImageDraw.Draw(outputImage)

for i in range(height):
    for j in range(width):
        rgb = []
        rgb = pixel[j, i]
        try:
            r = rgb[0]
            g = rgb[1]
            b = rgb[2]
            h = int(r/3 + g/3 + b/3)
        except:
            h = rgb
        pixel[j, i] = h
        text_file.write(getCHAR(h))
        d.text((j*oneCharWidth, i*oneCharHeight), getCHAR(h), font = font, fill = fill_rgb)

    text_file.write('\n')
# This code below will print your output image and save as a output.png 
outputImage.save('output.png')
time2 = time()
text_file.close()
print("finished in {} seconds".format(round(time2-time1,6)))