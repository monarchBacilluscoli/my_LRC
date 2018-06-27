from PIL import Image

path = "orl_faces\\s1\\1.pgm"
im = Image.open(path).getdata()

a = 1
b = 2
s = str(a)+'*'+str(b)
print(s)