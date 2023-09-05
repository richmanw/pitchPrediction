from batter import *
from pitcher import *


def main():

    balls = 0
    strikes = 0
    outs = 0

    batter_name = input("Batter Name: ")
    pitcher_name = input("Pitcher Name: ")

    scrapeProfile(batter_name)
    #scrapeProfile(pitcher_name)




main()
