import numpy as np
import matplotlib.pyplot as plt


iterations=500
from numpy import loadtxt
elapsed = loadtxt("SaveFiles/JetsonNano/test_HN2_32.txt", delimiter=" ", unpack=False)


x=range(iterations)
y=elapsed

plt.figure(figsize=(8, 8))
plt.plot(x, y)
plt.xlabel("Image")
plt.ylabel("Seconds")
plt.title('HN2 fp32 Processing Time /per Image')

plt.show()
