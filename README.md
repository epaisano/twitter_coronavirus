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
**Frequency of the #coronavirus Usage by Country in 2020**
<img src=covidfreqcountry2020.png width=100% />
Here, we see that amongst the top 10 countries that used the #coronavirus tag, the United States ranked at number one.
In fact, it beats Brazil, the runner-up country to the US, by almost 3000000 times. 

**Frequency of the #coronavirus Usage by Language in 2020**
<img src=covidfreqlang2020.png width=100% />
Of course, given that the tag is in english, we can expect for most of the tweets that used this tag were in english.
Further, this is also how the virus is spelled in spanish (represented by es for español), thus explaining why the second language that used it most in 2020 is spanish. 

**Frequency of the #코로나바이러스 Usage by Country in 2020**
<img src=covidmandfreqcountry2020.png width=100% />
Similar to the usage of the tag #coronavirus, tweets containing the tag #코로나바이러스 were also mostly sent from the United States, with Brazil as a runner up.
However, in this graph, we see that the tag was used about 500000 times less than the #coronavirus tag was used. 

**Frequency of the #코로나바이러스 Usage by Language in 2020**
<img src=covidmandfreqlang2020.png width=100% />
The tweets that used this tag were mostly in korean in the year 2020.
The frequency at which tweets that used this tag were written in korean far exceeds any other language.
In fact, it beats the runner up language, english, by about 200 tweets.

## Task 4 Plots

**Alternative Reduce Graph**
<img src=altreduce.png width=100% />
This graph shows us that amongst the hashtags seen in the legend, #corona was the most used in 2020 around mid-March.
This makes sense, as we know the beginning of our lockdown period was March 12, 2020.
Thus, we expect social media trended towards talk about coronavirus.
