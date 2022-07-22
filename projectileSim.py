from distutils.log import warn
import math
import time


class projectile:

    def simulate(intiCord, initVelocity, angle):
        tr = 0

        tr = time.time()

        # Initialize variables
        x = intiCord
        y = 0
        v = initVelocity
        theta = angle
        t = 0
        dashX = []
        dashY = []
        maxH = 0
        # Calculate trajectory
        while y >= 0:
            x = v * math.cos(theta) * t
            y = v * math.sin(theta) * t - (0.5 * 9.8 * t ** 2)
            if y > maxH:
                maxH = y
            if y > 100000:
                print("The projectile will not reach the ground.")
                break
            dashX.append(x)
            dashY.append(y)
            print("x = " + str(x) + ", y = " + str(y))
            t += 0.1
        tr = (time.time() - tr)*1000
        print("simulation Completed in " + str(tr) + " milliseconds")
        return {"type": "numarray", "x": dashX, "y": dashY, "maxH": maxH, "title": "Projectile Trajectory", "xlabel": "distance", "ylabel": "Height"}
