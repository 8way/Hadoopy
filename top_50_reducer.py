#!/usr/bin/python3

import sys
import operator
from collections import Counter



def read_map_output(file):
    """ Return an iterator for key, value pair extracted from file (sys.stdin).
    Input format:  key \t value
    Output format: (key, value)
    """
    for line in file:
        yield line.strip().split("\t")


def top_50_reducer():
    current_place_id = "-1"
    current_place_url = "-1"
    # current_place_type = "-1"
    isPlace = False
    pictureCount = {}
    place2tags = {}


    for placeid, photoid, tags, placeUrl in read_map_output(sys.stdin):
        if photoid == "-1":
            isPlace = True
        else:
            isPlace = False

        if isPlace: # Place
            if current_place_id != placeid:
                current_place_id = placeid
                current_place_url = placeUrl
        else: # Photo
            if current_place_id == placeid:
                pictureCount[current_place_url] = pictureCount.get(current_place_url, 0) + 1
                if current_place_url in place2tags:
                    place2tags[current_place_url] +=tags.split(",")
                else:
                    place2tags[current_place_url] = tags.split(",")

    pictureCount = sorted(pictureCount.items(), key = operator.itemgetter(1), reverse=True)
    for place, count in pictureCount[:50]:
        print(str(place)+"\t"+str(count)+"\t", str(Counter(place2tags.get(place)).most_common(10)).strip('[]'))



if __name__ =="__main__":
    top_50_reducer()
