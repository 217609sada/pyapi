#!/usr/bin/env python3

import yaml
import json

def main():
    hitchhikers = [
            {"name": "Zaphod Bebble",
                "species": "Bete"},
            {"name": "Arthur",
                "species": "human"}
            ]

    #print(hitchhikers)

    zfile = open("galaxyguide.yaml", "w")

    yaml.dump(hitchhikers, zfile)

    zfile.close()

    yamlstring = yaml.dump(hitchhikers)
    
    #print(yamlstring)

    with open("galaxyguide.yaml", "r") as ip_file:
        pyyammy = yaml.load(ip_file)
        print("Before")
        print(pyyammy)
        print("After")
        pyyammy.append({"service": "Identity", "app": "keystone"})
        print(pyyammy)
        ip_file.close()

    with open("vcp.json", "w") as vcp_json:
        json.dump(pyyammy, vcp_json)

main()
