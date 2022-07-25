
try:
    import matplotlib.pyplot as plt
except ImportError:
    from packageManager import packageManager as packMan
    packMan.install("matplotlib")
    import matplotlib.pyplot as plt


def plot(obj):
    arrayX = []
    arrayY = []
    t = 0
    # split object["type"] by _
    objType = obj["type"].split("_")
    if objType[0] == "numarray":
        if objType[1] == "increment":
            for i in range(int(round(obj["time"]/obj["increment"]))):
                t = round(t, 2)
                arrayX.append(obj["data"][i][t]["x"])
                arrayY.append(obj["data"][i][t]["y"])
                t += obj["increment"]
            plt.plot(arrayX, arrayY)
            plt.show()


print("☺️")
