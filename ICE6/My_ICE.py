#
# # Import the necessary packages and modules
# import matplotlib.pyplot as plt
# import numpy as np
#
# # Prepare the data
# x = np.linspace(0, 10, 100)
#
# # Plot the data
# plt.plot(x, x, label='linear')
#
# # Add a legend
# plt.legend()
#
# # Show the plot
# plt.show()

import numpy as np
from sklearn import linear_model
import matplotlib. pyplot as plt
#
# x = np. linspace (0 , 5, 1000)
# y = np.power(x , 4)
# plt. plot (x , y)
# plt.show()
# create x and y

x = np.array([0,1,2,3,4,5,6,7,8,9])
y = np.array([1,3,2,5,7,8,8,9,10,12])

m_X = np.mean(x)
m_Y = np.mean(y)

B1 = np.sum((x - m_X) * (y - m_Y)) / np.sum(np.square(x - m_X))

B0 = m_Y - B1 * m_X

plt.scatter(x, y, color='red')

z = [B1*i + B0 for i in x]
plt.plot(x, z)
plt.title(B1)
plt.show()
