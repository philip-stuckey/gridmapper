import maidenhead
from maiden_region import dimension
import math

from sys import argv  # I'm getting lazy
earth_radius_mi=3958.8

(lat, lon) = maidenhead.to_location(argv[1], center=True)
(width, height) = dimension(argv[1])
width_mi = earth_radius_mi*math.cos(math.radians(lat))*math.radians(width)

scale = 10**round(math.log10(width_mi/5))

print(scale,'M', sep='')

