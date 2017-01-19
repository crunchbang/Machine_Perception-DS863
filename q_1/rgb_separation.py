import cv2
from matplotlib import pyplot as plt

orig = cv2.imread('sample.jpg', cv2.IMREAD_COLOR)
blue_channel, green_channel, red_channel = cv2.split(orig)
#cv2 represents images as (B,R,G) while matplotlib uses (R,G,B)
orig = orig[:, :, ::-1] # inverts the ordering of the channels

fig = plt.figure()

channels = [orig, red_channel, green_channel, blue_channel]
channels_title = ["Original", "Red channel", "Green channel", "Blue channel"]

for i in range(4):
    ax = fig.add_subplot(2, 2, i+1)
    ax.set_title(channels_title[i])
    ax.imshow(channels[i], cmap="gray")
    plt.xticks([])
    plt.yticks([])
plt.show()

