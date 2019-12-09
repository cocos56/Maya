import os
import cv2
from PIL import Image
from pic import recreatePath
from pic import toHP
from pic import toGray
from pic import trans

sourceFileName='a' #要提取视频的文件名，隐藏后缀

times=0 #提取视频的频率，每50帧提取一个
bannedFrames = [11, ]
bannedFrames = []

outPutDirName = sourceFileName+'_RGB/'
grayDirName = sourceFileName+'_gray/'
HPDirName = sourceFileName+'_HP/'

outPutTDirName = sourceFileName+'_RGB_T/'
grayTDirName = sourceFileName+'_gray_T/'
HPTDirName = sourceFileName+'_HP_T/'

recreatePath(outPutDirName, outPutTDirName, grayDirName, grayTDirName, HPDirName, HPTDirName)

camera = cv2.VideoCapture(sourceFileName+'.mp4')

while True:
	times+=1
	res, image = camera.read()
	if not res: print('end');break
	if times in bannedFrames: continue

	cv2.imwrite(outPutDirName + str(times)+'.jpg', image)

	img = Image.open(outPutDirName + str(times)+'.jpg')
	trans(img, outPutTDirName + str(times)+'.jpg')

	im = toGray(img, grayDirName + str(times)+'.jpg')
	trans(im, grayTDirName + str(times)+'.jpg')

	im = toHP(img, HPDirName + str(times)+'.jpg')
	trans(im, HPTDirName + str(times)+'.jpg')

	print(outPutDirName + str(times)+'.jpg')
camera.release()
print('图片提取结束')