#!/usr/bin/env python3

import json

def main():
    with open("datacenter.json", "r") as datacenter:
        datacentrestring = datacenter.read()

    print(datacentrestring)
    print(type(datacentrestring))
    print("\nThe code above is string data. Python cannot easily work with this data. ")
    input("Press enter to continue\n")

    datacenterdecoded = json.loads(datacentrestring)

    print(type(datacenterdecoded))

    print(datacenterdecoded)

    print(datacenterdecoded["row3"])

    print(datacenterdecoded["row2"][0])
        
main()
