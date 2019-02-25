import pandas as pd
from ipyleaflet import Marker, Map, MarkerCluster

det_info ="Data.csv"
detector_information = pd.read_csv(det_info)

center = (-37.814 , 144.96332) #This is the lat long of Melbourne

def GPS(n):
    Coordinates = detector_information.set_index("Short Name")[["Y","X"]]
    return {"Name" : Coordinates.index[n], "GPS" :(Coordinates.Y[n], Coordinates.X[n])}

Detectors = {}

Detectors[0] = { "Name" : "14352OB_L1P0",
                "GPS" : (-37.735018, 144.894947)
               }
Detectors[1] = { "Name" : "14352OB_L1P1",
                "GPS" : (-37.735012, 144.894879)
               }




m = Map(center=center, zoom=11)


marker1 = Marker(location=Detectors[0].get("GPS"), draggable=False)
marker2 = Marker(location=Detectors[1].get("GPS"), draggable=False)

marker_cluster = MarkerCluster(
    markers=(marker1, marker2)
)

m.add_layer(marker_cluster);

m