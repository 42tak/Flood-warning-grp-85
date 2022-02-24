"""Unit test for the flood module"""

from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level

def test_stations_level_over_threshold():
    """2B-Checks the output is a list
    Checks the list contains tuples
    Checks the tuples contain a monitoring station object and a float
    Checks the float is greater than the tol given"""

    stations = build_station_list()
    update_water_levels(stations)
    above_tol = stations_level_over_threshold(stations, 0.9)
    assert type(above_tol)==list
    for foo in above_tol:
       assert type(foo)==tuple
       assert type(foo[0])==MonitoringStation
       assert type(foo[1])==float
       assert foo[1]>0.9

