import matplotlib.pyplot as plt
import numpy as np
import imageio

insect = imageio.imread('./insect.jpg')
insect.shape 
# imageio.imwrite('./insect.jpg', insect[:, :, 0])


plt.figure()
plt.gray()

plt.subplot(121)
plt.imshow(insect)

zinsect = insect[100:350,140:350]

plt.subplot(122)
plt.imshow(zinsect)

plt.show()

