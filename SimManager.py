

import json


def SaveSimulation(simulation, env="int"):
    if env == 'int':
        line1 = "#!/usr/bin/env python3\n"
        line2 = "simulation = " + str(simulation) + "\n"
        line3 = "plot(simulation, 'Save')\n"
        # create a file with the name of the simulation
        with open(simulation["title"] + ".py", "w") as file:
            file.write(line1)
            file.write("from plotter import *\n")
            file.write(line2)
            file.write(line3)
            file.close()

    elif env == 'ext':

        fileCtx = "#!/usr/bin/env python3\ntry:\n    import matplotlib.pyplot as plt\nexcept ImportError:\n    import pip as pip\n    pip.main(['install', 'matplotlib'])\n    import matplotlib.pyplot as plt\n"
        line2 = "simulation = " + str(simulation) + "\n"
        fileCtx += line2
        fileCtx += "arrayX = []\narrayY = []\nt = 0\n"
        fileCtx += "objType = simulation['type'].split('_')\n"
        fileCtx += "if objType[0] == 'numarray':\n    if objType[1] == 'increment':\n        for i in range(int(round(simulation['time']/simulation['increment']))):\n            t = round(t, 2)\n            arrayX.append(simulation['data'][i][t]['x'])\n            arrayY.append(simulation['data'][i][t]['y'])\n            t += simulation['increment']\n        plt.title(simulation['title'])\n        plt.xlabel(simulation['xlabel'])\n        plt.ylabel(simulation['ylabel'])\n        plt.plot(arrayX, arrayY)\n        plt.savefig(simulation['title'] + '.png')\n"
        with open(simulation["title"] + ".py", "w") as file:
            file.write(fileCtx)
            file.close()
    elif env == 'csv':
        ctx = ""
        with open(simulation["title"] + ".csv", "w") as file:
            t = 0
            file.write("t,x,y\n")
            for i in range(int(round(simulation["time"]/simulation["increment"]))):
                t = round(t, 2)
                x = simulation["data"][i][t]["x"]
                y = simulation["data"][i][t]["y"]
                file.write(str(t)+","+str(x)+","+str(y)+"\n")
                t += simulation["increment"]
            file.close()
    elif env == 'json':
        with open(simulation["title"] + ".json", "w") as file:
            json.dump(simulation, file)
            file.close()
