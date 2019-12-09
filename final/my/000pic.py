import os
from PIL import Image

files = os.listdir()
pics=[]
for i in files:
	ext = os.path.splitext(i)[1]
	if ext=='.jpg': pics.append(i)

for i in pics:
	print(i)
	img = Image.open(i)
	img=img.transpose(Image.ROTATE_270)
	img=img.transpose(Image.ROTATE_180)
	img.save(i)
print('end')