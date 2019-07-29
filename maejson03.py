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

    jsonstrings = json.dumps(hitchhikers)

    print(type(hitchhikers))
    print(hitchhikers[0])

    print(type(jsonstrings))
    print(jsonstrings)
        
main()
