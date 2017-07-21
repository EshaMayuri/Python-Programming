import csv
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

dates = []
volume = []

# Opening file and reading it
def fetchData(filename):
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)
        for row in csvFileReader:
            dates.append(int(row[0]))
            volume.append(int(row[6]))
    return
fetchData('yahooHistData.csv')

linear = linear_model.LinearRegression()
dates = np.reshape(dates, (len(dates), 1))
volumes = np.reshape(volume, (len(volume), 1))
linear.fit(dates, volumes)
plt.scatter(dates, volumes, color='red')
plt.plot(dates, linear.predict(dates), color='blue')
plt.title("Linear regression Yahoo historical data!")
plt.show()

predicted_volumes = linear.predict(10)

print("The volume predicted for 10 June is: $", str(predicted_volumes[0][0]))
