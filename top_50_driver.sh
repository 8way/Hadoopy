#!/bin/bash

if [ $# -ne 3 ]; then
    echo "Invalid number of parameters!"
    echo "Usage: ./top_50_driver.sh [input_location] [input_location] [output_location]"
    exit 1
fi

hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
-D mapreduce.job.reduces=3 \
-D mapreduce.job.name='Tag owner inverted list' \
-file top_50_locality.py \
-mapper top_50_locality.py \
-file top_50_reducer.py \
-reducer top_50_reducer.py \
-input $1 \
-input $2 \
-output $3
