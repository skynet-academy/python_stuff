import scipy.misc
import matplotlib.pyplot as plt
from PIL import Image

im = Image.open('map_zone.bmp')

plt.imshow(im)
plt.show()
print(im.format, im.size, im.mode)


