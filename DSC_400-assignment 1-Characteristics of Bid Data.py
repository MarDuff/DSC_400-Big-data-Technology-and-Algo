#!/usr/bin/env python
# coding: utf-8

# In[1]:


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

# In[12]:


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
