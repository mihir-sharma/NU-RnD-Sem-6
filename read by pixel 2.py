import cv2

blue= open('blue.txt', 'w')
green= open('green.txt', 'w')
red= open('red.txt', 'w')
x=input("Enter path of image")
img = cv2.imread(x)

height, width, channels  = img.shape
print(str(height) + ' ' + str(width))

for i in range(0, height):
    for j in range(0,width):
        b=img[i,j,0]
        g=img[i,j,1]
        r=img[i,j,2]
        blue.write(str(b) + '\n')
        green.write(str(g) + '\n')
        red.write(str(r) + '\n')

blue.close()
green.close()
red.close()
