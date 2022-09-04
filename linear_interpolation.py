
#LAB 3-FAISHAL KAMIL
# Python code in case you want to follow along

# Importing Python packages
import pandas as pd
import matplotlib.pyplot as plt

# Creating the data
hours = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.]
temperature_celcius = [22, 20.5, 19, 18.5, 18, 18, 18.5, 19, 21, 23, 24, 24.5, 25, 26, 27, 28, 28, 26, 24.5, 23, 22, 22, 21.5, 21, 22]

# Creating a pandas dataframe 
data = pd.DataFrame({'hours': hours, 'temp': temperature_celcius }) 

# Import Python packages for interpolation
import numpy as np
import scipy.interpolate as interpolate

# Create a linear interpolation function based on the originay data
linear_interpolation_func = interpolate.interp1d(data.hours, data.temp, kind='linear')

# Create a list with 10 'time' values per hour (6-minute interval)
half_hour_scale = np.linspace(0., 24., 24*1)

# Interpolate the temperature on the 6-minute scale
linear_interpolated_y = linear_interpolation_func(half_hour_scale)

#plot the result
plt.figure(figsize=(12,10))
plt.scatter(data.hours, data.temp)
plt.scatter (half_hour_scale, linear_interpolated_y)
plt.plot(half_hour_scale, linear_interpolated_y, 'red')
plt.legend(['Linear Interpolation', 'Original'])
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.show()
