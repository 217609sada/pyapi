#!/usr/bin/env python3

def main():
    
    hostipdict = {
            'host01': '10.1.2.3', 
            'host02': '10.2.3.4', 
            'host03': '5.1.2.3'
            }
    
    print(hostipdict['host02'])

    hostipdict['host04'] = '172.0.0.1'

    print(hostipdict)

    hostipdict.update({'host05': '1.2.3.4'})

    print(hostipdict)

main()


