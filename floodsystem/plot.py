import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from floodsystem.analysis import polyfit
from floodsystem.stationdata import build_station_list

def plot_water_levels(station, dates, levels):

    # Plot
    plt.plot(dates, levels)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title("Station " + station)
    
    plt.show()
    
    stations = build_station_list()
    station_range=[]
    station_dates=[]
    for station in stations:
        if station.typical_range != None:
            station_range.append(station.typical_range)
   
    total_station_values = len(station_range)
    print(total_station_values)

    #finding the typical low values
    i = 0
    print("a") #to check where i am
    sum_of_low_values = 0
    while (i < 10):                  #will take too long to iterate through all values
        sum_of_low_values += station_range[i][0] + station_range[i+1][0]
        i+=1
    print(sum_of_low_values)
    mean_low_value = sum_of_low_values / total_station_values
    print(mean_low_value)
    plt.axhline(y=mean_low_value)
    
     #finding the typical high values
    j = 0
    print("b")     #to check where i am
    sum_of_high_values = 0
    while (j < 10):                #will take too long to iterate through all values
        sum_of_high_values += station_range[j][1] + station_range[j+1][1]
        j+=1
    print(sum_of_low_values)
    mean_high_value = sum_of_high_values / total_station_values
    print(mean_high_value)
    plt.axhline(y=mean_high_value)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()
    
 def plot_water_levels_with_fit(station, dates, levels, p):
    station_name = str(station)
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title("Station " + station_name)

    # Plot original data points
    plt.plot(dates, levels)
    
    # Plot polynomial fit at 30 points along interval
    float_dates = matplotlib.dates.date2num(dates)
    x1 = np.linspace(float_dates[0], float_dates[-1], 30)
    p_coeff = np.polyfit(float_dates, levels, p)
    poly = np.poly1d(p_coeff)
    plt.plot(x1, poly(x1 - float_dates[0]))

    # Display plot
    plt.show()
   
    
