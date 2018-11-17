from poliastro.bodies import Earth, Mars, Venus
from .poliastro_handler import *
from astropy.time import Time
from datetime import datetime

# Development ---------------------------------------------------------------------------------------------------------#
if __name__ == "__main__":

    print(body_2_barycentric_posvel(Earth, time=Time(datetime(2018, 12, 2, 2))))
