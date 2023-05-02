# Coronavirus Twitter Analysis

We analyze the frequency of usage of geotagged tweets sent in 2020 mentioning the coronavirus.

## Background

**About the Data:**

Approximately 500 million tweets are sent everyday.
Of those tweets, about 2% are *geotagged*.
That is, the user's device includes location information about where the tweets were sent from.
The lambda server's `/data/Twitter dataset` folder contains all geotagged tweets that were sent in 2020.
In total, there are about 1.1 billion tweets in this dataset.

The tweets are stored as follows.
The tweets for each day are stored in a zip file `geoTwitterYY-MM-DD.zip`,
and inside this zip file are 24 text files, one for each hour of the day.
Each text file contains a single tweet per line in JSON format.
JSON is a popular format for storing data that is closely related to python dictionaries.


**About MapReduce:**

To analyze said tweets, we followed the MapReduce procedure.
MapReduce is a famous procedure for large scale parallel processing that is widely used in industry.
It is a 3 step procedure consisting of the following:

1. Partition
1. Map
1. Reduce


## Task 3 Plots

<img src=covidfreqcountry2020.png width=100% />
<img src=covidfreqlang2020.png width=100% />
<img src=covidmandfreqcountry2020.png width=100% />
<img src=covidmandfreqlang2020.png width=100% />
