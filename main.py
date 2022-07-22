import time
from projectileSim import projectile as pJ
from packageManager import packageManager as packMan
from converter import converter as conv
from plotter import *


class main:
    def __init__(self):
        self.__main()

    def __main(self):
        print("Hello and welcome to SimuleX Suite!")
        print("to install nessecary packages , type in install")
        b = input("")
        if b == "install" or b == "INS":
            print("checking for packages...")
            packMan.install()
            print("done")
        else:
            print("invalid input")
            print("exiting...")
            exit()


plot(pJ.simulate(0, 1009, conv.getradians(45)))
