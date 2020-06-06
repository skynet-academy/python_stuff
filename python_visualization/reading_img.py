import scipy.misc
import matplotlib.pyplot as plt

# load already prepared ndarray from scipy

ascent = scipy.misc.ascent()
face = scipy.misc.face()
# set the default colormap to gray

plt.gray()

plt.imshow(face)
plt.show()



plt.gray()

plt.imshow(ascent)
plt.colorbar()
plt.show()

