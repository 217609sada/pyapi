#!/usr/bin/env python3

import json

def main():
    hitchhikers = [
            {
                "name": "zaphod Beeblebrox", 
                "species": "Betlegueisn"
                }, 
            {
                "name": "Arthur", 
                "species": "Human"
                }
            ]

    print(hitchhikers)

    with open("galaxyguide.json", "w") as zfile:
        json.dump(hitchhikers, zfile)
        
main()
