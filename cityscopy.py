#!/usr/bin/python

import argparse
from cityscopy.Scanner.Scanner import Scanner
from cityscopy.Setup.Setup import Setup
import sys
import os


def main():

    parser = argparse.ArgumentParser(
        prog="cityscopy",
        description="CityScoPY: A Scanner for MIT CityScope",
        epilog="Thank you for using CityScope!",
    )

    parser.add_argument('--cityscopy', '-c',
                        default=None,
                        required=True,
                        const='all',
                        nargs='?',
                        choices=['scan', 'keystone', 'setup'],
                        help='list servers, storage, or both (default: %(default)s)')

    parser.add_argument('--table_name', '-t',
                        action='store',
                        required=True,
                        help='table\'s name')
    args = parser.parse_args()

    # get the table name and make it lower case
    args.table_name = args.table_name.lower()

    # run the right command based on the input argument
    if args.cityscopy == 'scan':
        scanner = Scanner(CITYSCOPE_PRJ_NAME=args.table_name)
        scanner.scan()

    elif args.cityscopy == 'setup':
        setup = Setup(CITYSCOPE_PRJ_NAME=args.table_name)
        setup.setup()

    else:
        parser.print_help()
        sys.exit(1)

    #! start local UDP comms
    # # cityscopy.udp_listener()
        
    # #! HTTPを使ってデータを送信する
    # PS C:\cityscope_methods\CS_CityScoPy-master\CS_CityScoPy-master> python cityscopy.py -c scan -t test


if __name__ == '__main__':
    # os.system('cls' if os.name == 'nt' else 'clear') # clear the terminal
    print("cityscopy: A Scanner for CDL")
    main()
    
        # '''
        # >>>>>> CityScoPY: A Scanner for MIT CityScope >>>>>>>>


        #                     |||||||||||
        #                     |||||||||||
        #                             |||
        #                             |||
        #                             |||
        #                     |||      ||||||||||||
        #                     |||      ||||||||||||
        #                     |||               |||
        #                     |||               |||
        #                     |||               |||
        #                     ||||||||||||      |||
        #                     ||||||||||||      |||



        # Copyright (C) {{ 2018 - 2023 }}  {{ Ariel Noyman }}

        # Ariel Noyman
        # https://github.com/CityScope/
        # http://arielnoyman.com
        # https://github.com/RELNO

        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # '''
# 1871.0  -43.0  -68.0  -54.0  1971.0  1045.0  -48.0  1073.0"


# "types": {"Campus": {"name": "Campus", "color": [171, 143, 57], "height": [0, 15, 30], "cityscopy_id": 0, "cityscopy_pattern": "0000000000000000"}, 
#             "Office": {"name": "Office", "color": [36, 130, 198], "height": [0, 50, 100], "cityscopy_id": 1, "cityscopy_pattern": "0000000000000001"}, 
#             "Park": {"name": "Park", "color": [126, 179, 70], "height": [0, 0, 0], "cityscopy_id": 2, "cityscopy_pattern": "0000000000000010"}, 
#             "Residential": {"name": "Residential", "color": [185, 126, 24], "height": [0, 50, 100], "cityscopy_id": 3, "cityscopy_pattern": "0000000000000011"}}}