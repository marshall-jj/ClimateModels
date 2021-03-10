import matplotlib.pyplot as plt
plt.style.use('seaborn')

import numpy as np


grid_points = 10 # number of grid points
domain_width = 1e6 # meters
cell_width = domain_width / grid_points # meters

time_step = 100 # years
years = 20000 
n_steps = int(years/ time_step)

flow_param = 1e4 # m horizontal / yr
snowfall = 0.5 # m / y

plot_limit = 4000 # m


elevations = np.zeros(grid_points+2)
flows = np.zeros(grid_points+1)

plt.figure(figsize=(20,10))
plt.title('Evolution of an Ice Sheet Over 20 000 Years')
plt.xlabel('Ice Sheet Width /x10$^6$ m')
plt.ylabel('Elevation /m')
plt.ylim(0, plot_limit)


for step in range(0, n_steps):

    for ix in range(0, grid_points + 1):
        flows[ix] = (elevations[ix] - elevations[ix+1]) / cell_width * flow_param  * (elevations[ix] + elevations[ix+1]) / 2 / cell_width

    for ix in range(1, grid_points + 1): # range starts at 1 to avoid the first 0 in the array which needs to be kept at 0
         elevations[ix] = elevations[ix] + (snowfall + flows[ix-1] - flows[ix]) * time_step

    plt.plot(elevations)
    plt.pause(0.01)

plt.show()
