from math import *
from unimodal_segments_lookup import get_unimodal_segments

f = lambda x: 3+cos(2*pi*x)+2*sin(2*pi*x)+5*cos(3*pi*x)+4*sin(3*pi*x)
unimodal_segments = get_unimodal_segments(f, -1, 1, 0.001)
print(unimodal_segments)
