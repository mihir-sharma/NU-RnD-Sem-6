from PIL import Image
f=open('pixel value file.txt' , 'w')
im = Image.open(r"<path of image file here>")
pix = im.load()
x= im.size
print(x)
for i in range(0,1024):
    f.write('\n')
    for j in range(0,768):
        y=str(pix[i,j])
        f.write(y + '\t')
f.close()
im.close()
