import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "image path")
args = vars(ap.parse_args())

img = cv2.imread(args["image"])
green = [50,60,60]

diff = 49

boundaries = [([green[2] - diff, green[1] - diff, green[0] - diff], [green[2] + diff, green[1] + diff, green[0] + diff])]

lower = boundaries[0][0]
upper = boundaries[0][1]
lower = np.array(lower, dtype="uint8")
upper = np.array(upper, dtype="uint8")
mask = cv2.inRange(img, lower, upper)

ratio_g = cv2.countNonZero(mask)/(img.size/3)
n = args["image"].find(".png")
n = args["image"][:n]
print(args["image"],n, np.round(ratio_g*100,2),sep=",")



