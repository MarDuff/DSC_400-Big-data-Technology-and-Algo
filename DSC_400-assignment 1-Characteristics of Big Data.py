#!/usr/bin/env python
# coding: utf-8

# In[3]:


# This code helps check asssignment data

import pandas as pd
from collections import namedtuple
from dataclasses import dataclass

InformationUnit = namedtuple('InformationUnit', ['name', 'size'])
DataItem = namedtuple('DataItem', ['name', 'size', 'unit'])
LatencyItem = namedtuple('LatencyItem', ['name', 'time', 'unit', 'explanation'])

information_units = dict(
    B=InformationUnit("byte", 1),
    KB=InformationUnit("kilobyte", 1e3),
    MB=InformationUnit("megabyte", 1e6),
    GB=InformationUnit("gigabyte", 1e9),
    TB=InformationUnit("terabyte", 1e12),
    PB=InformationUnit("petabyte", 1e15),
    EB=InformationUnit("exabyte", 1e18),
    ZB=InformationUnit("zettabyte", 1e21),
    YB=InformationUnit("yottabyte", 1e24)
)

time_units = {
    "ms": "millisecond",
    "s": "second",
    "min": "minute"
}

def check_data_items(items):
    # Checks to see if data sizes and units are filled out correctly
    for item in items:
        assert item.size > 0, 'Size for "{}" should be greater than zero'.format(item.name)
        assert item.unit in information_units, 'Unit "{}" not in units dictionary'.format(item.unit)
        
def check_latency_items(items):
    # Checks to see if time sizes and units are filled out correctly
    for item in items:
        # assert item.time > 0, 'Time for "{}" should be greater than zero'.format(item.name)
        assert item.unit in time_units, 'Unit "{}" not in time units dictionary'.format(item.unit)
        assert item.explanation != "FILL IN THE EXPLANATION HERE", 'Fill in explanation for "{}"'.format(item.name)


# ### Assignment 1.1

# In[4]:


# TODO: Fill in the estimated sizes for each item
# You may need to adjust the units as well

items1_1 = [
    DataItem('1 Byte', 1, 'B'),
    DataItem("128 character message", 128, "B"),
    DataItem("1024x768 PNG image", 3, "MB"),
    DataItem("1024x768 RAW image", 3, "MB"),
    DataItem("HD (1080p) HEVC Video (15 minutes)", 2.20, "GB"),
    DataItem("HD (1080p) Uncompressed Video (15 minutes)", 209, "MB"),
    DataItem("4K UHD HEVC Video (15 minutes)", 4.8, "GB"),
    DataItem("4k UHD Uncompressed Video (15 minutes)", 34, "GB"),
    DataItem("Human Genome (Uncompressed)", 700, "MB"),
]

# Checks if items properly updated
check_data_items(items1_1)
    
df1_1 = pd.DataFrame(items1_1)
df1_1


# ### Assignment 1.2

# In[22]:


# TODO: Fill in the estimated sizes for each item
# You may need to adjust the units as well

items1_2 = [
    DataItem("Daily Twitter Tweets (Uncompressed)", 500*1e6*128, "B"),
    DataItem("Daily Twitter Tweets (Snappy Compressed)", 200*1e6*128, "B"),
    DataItem("Daily Instagram Photos", 100*1e6*3*0.75, "B"),
    DataItem("Daily YouTube Videos", 500*3*24, "MB"),
    DataItem("Yearly Twitter Tweets (Uncompressed)", 500*1e6*365*128, "B"),
    DataItem("Yearly Twitter Tweets (Snappy Compressed)", 200*1e6*365*128, "B"),
    DataItem("Yearly Instagram Photos", 100*1e6*3*365, "B"),
    DataItem("Yearly YouTube Videos", 500*3*24*365, "B"),
]

# Checks if items properly updated
check_data_items(items1_2)

df1_2 = pd.DataFrame(items1_2)
df1_2


# ### Assignment 1.3

# In[5]:


# TODO: Provide explanations for how you arrived at each estimation

los_angeles_to_amsterdam_explanation = """
Typically around 150-200 milliseconds (ms) for a direct data transmission through undersea fiber optic cables
"""
low_earth_orbit_satellite_explanation = """
Roughly 2 milliseconds (ms) or less, 
considering the shorter distance from Earth's surface to a LEO satellite, 
usually about 1,200 kilometers (750 miles) above the Earth.
"""
geostationary_satellite_explanation = """
Around 500 milliseconds (ms) or more due to the greater distance, 
typically positioned at an altitude of approximately 35,786 kilometers (22,236 miles) above the equator.
"""
earth_to_the_moon_explanation = """
Approximately 1.28 seconds (1,280 milliseconds) for the transmission of data between Earth and the Moon, 
accounting for an average distance of about 384,400 kilometers (238,855 miles).
"""
earth_to_mars_explanation = """
At its closest approach (closest approach or opposition), 
the one-way signal can take around 3 to 22 minutes, and at the farthest point (aphelion), 
it can take up to about 48 minutes one way.
These figures are based on the average distance between Earth and Mars, 
which is about 54.6 million kilometers (33.9 million miles)
"""

# TODO: Fill in the estimated times for each item

items1_3 = [
    LatencyItem(
        "Los Angeles to Amsterdam",
        200,
        "ms",
        los_angeles_to_amsterdam_explanation.strip()
    ),
    LatencyItem(
        "Low Earth Orbit Satellite",
        2,
        "ms",
        low_earth_orbit_satellite_explanation.strip()
    ),
    LatencyItem(
        "Geostationary Satellite",
        500,
        "ms",
        geostationary_satellite_explanation.strip()
    ),
    LatencyItem(
        "Earth to the Moon",
        1.28,
        "s",
        earth_to_the_moon_explanation.strip()
    ),
    LatencyItem(
        "Earth to Mars",
        48,
        "min",
        earth_to_mars_explanation.strip()
    ),
]

# Checks if items properly updated
check_latency_items(items1_3)

df1_3 = pd.DataFrame(items1_3)
df1_3

