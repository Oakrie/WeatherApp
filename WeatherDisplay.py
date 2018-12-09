#Created by Tim Vela, Dec 8 2018
#!/usr/bin/env python3
import sys
import json
import logging
from ApiCall import weatherApi

# global define logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='/Users/timvela/Documents/logging/weatherApp.log',
                    filemode='w')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
logger = logging.getLogger('weatherApp')



def usage():
    print("All you need to do is run the program, no system arguments needed!")


def city_select():

    app = weatherApi()
    weatherData = app.get_weather("5992996")
    logger.error(weatherData)

def main():

    # define logging file


    if len(sys.argv) != 1:
        logger.error('Too many system arguments, Stopping program.')
        usage()

    city_select()


if __name__ == "__main__":
    main()
