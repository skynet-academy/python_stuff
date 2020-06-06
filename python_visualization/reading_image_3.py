import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

insect = Image.open('./insect.jpg')
arr = np.array(insect.getdata(), np.uint8).reshape(insect.size[1], insect.size[0], 3)

plt.gray()
plt.imshow(arr)
plt.colorbar()
plt.show()

