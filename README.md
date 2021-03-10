# ClimateModels

## Description
A series of basic climate models which made up the 'Global Warming II' course offered by Coursera.

### naked_planet
* Simulates how the planetary temperature of a naked planet (planet with no greenhouse gases) would change through time as it approaches equilibrium.
* Temperature rises until it reaches a point where the energy out (calculated via black body) equals the energy in and the model reaches equalibrium.
* The heat capacity of the planet is set by a layer of water.

### ice_albedo_feedback
* Simulates the presence of ice around the world and planetary temperature in relation to changing solar constants.
* The code runs 2 while loops. One with increasing solar radiation, the other with decreasing. This is to demonstrate the hysteresis in the model. That is it takes more energy to come out of the snowball earth than it took to go into it because the ice sheet perpetuates its own existence due its high albedo.

### ice_sheet_flow
* Shows the evolution of an icesheet of fixed width over time based on snowfall and flow rates.
* The model works by splitting the icesheet into 10 cells then calculating the flow rate and elevation of each cell overtime.

### shallow_water
* Simulates the flow patterns of a fluid which starts with a column of water in the middle of a 15x15 grid.
* The flow in the model is driven by differences in the elevation of the water surface, which arise from the flow itself. The flow is also altered by rotation, accounting for the Coriolis effect on a rotating planet.
* The water is assumed to be homogeneous in the vertical (no differences in temperature, density, or velocity). This vertical homogeneity is what gives the model its name. 

### near_future
* Predicts and compares the CO2 concentrations, radiative forcing and surface temperature changes for 2 scenarios, business as usual and a world without us (starting 2015).
* The model demonstrates the slow drawdown rate of CO2 and the temporary increase in surface temperture in a world without us due to the absense of human-made aerosols.
