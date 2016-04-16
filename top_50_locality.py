#!/usr/bin/python3

import sys

def top_50_mapper():
    """This Mapper select photo_id tags and place_id
    Input format Photo: photo_id \t owner \t tags \t date_taken \t place_id \t accuracy
    Input format place: place_id \t woeid \t latitude \t longitude \t place-name \t place-type-id \t place-url
    Output format: place_id \t photo_id \t tags \t placeUrl
    """
    

    for line in sys.stdin:
        parts = line.strip().split("\t")
        place_id = -1
        placeType = -1
        placeUrl = -1
        # placeName = -1
        photo = -1
        tags = []

        if len(parts) == 6: # Photo
            photo = parts[0].strip()
            tags = parts[2].strip().split()
            place_id = parts[4].strip()
        elif len(parts) == 7: # Place
            place_id = parts[0].strip()
            # placeName = parts[4].strip()
            placeType = parts[5].strip()
            placeUrl = parts[6].strip()
        else:
            print("bad format not picture nor place")
            continue
        if placeType == "22":
            placeType = "7"
            placeUrl= parts[4].strip()[:parts[4].strip().rfind("/")]

        if placeType == "7" or placeType == -1:
            print("{}\t{}\t{}\t{}".format(place_id, photo, ','.join(tags), placeUrl))

if __name__ == "__main__":
    top_50_mapper()
