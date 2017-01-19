import cv2
from matplotlib import pyplot as plt

img_bgr = cv2.imread('sample.jpg', cv2.IMREAD_COLOR)
img = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB) # for displaying correctly with matplotlib

img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
hue, saturation, variance = cv2.split(img_hsv)

channel_image = [img, hue, saturation, variance]
channel_title = ["Original", "Hue channel", "Saturation channel", "Variance channel"]
channel_cmap = ["gray", "hsv", "gray", "gray"] #the correct color map is needed to get the required output

fig = plt.figure()

for i in range(4):
    ax = fig.add_subplot(2, 2, i + 1)
    ax.set_title(channel_title[i])
    ax.imshow(channel_image[i], cmap=channel_cmap[i])
    plt.xticks([]) # remove axis markings
    plt.yticks([])

img_hls = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)
hue, luminance, saturation  = cv2.split(img_hls)

channel_image = [img, hue, saturation, luminance]
channel_title = ["Original", "Hue channel", "Saturation channel", "Luminance channel"]
channel_cmap = ["gray", "hsv", "gray", "gray"]

fig = plt.figure()

for i in range(4):
    ax = fig.add_subplot(2, 2, i + 1)
    ax.set_title(channel_title[i])
    ax.imshow(channel_image[i], cmap=channel_cmap[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
