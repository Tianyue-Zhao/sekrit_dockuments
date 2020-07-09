import numpy as np
import cv2

mapped_points = np.loadtxt('mapped_points.txt')
mapped_points = mapped_points.astype('int')
saved_map = np.loadtxt('../../tools/berlin_blurred.txt')

frame = np.ones((600,600,3))*255
frame = frame.astype('uint8')

total = 0
for i in range(mapped_points.shape[0]):
    try:
        frame[mapped_points[i,0],mapped_points[i,1],:] = 0
        total += saved_map[mapped_points[i,0],mapped_points[i,1]]
    except:
        continue
print(total)

cv2.imwrite('mapped_points.png',frame)
