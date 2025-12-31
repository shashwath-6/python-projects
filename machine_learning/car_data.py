import matplotlib.pyplot as plt
import pandas as pd

cars = ['AUDI', 'BMW', 'FORD',
'TESLA', 'JAGUAR',]
data1 = [23, 10, 35, 15, 12]
plt.pie(data1, labels=cars)
plt.title("Car data")
plt.show()