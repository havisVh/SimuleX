
try:
    import matplotlib.pyplot as plt
except ImportError:
    from packageManager import packageManager as packMan
    packMan.install("matplotlib")
    import matplotlib.pyplot as plt


def plot(obj, ask='else', path='/'):
    if ask == "Save":
        SaveImage(obj, path)
    else:
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
                plt.title(obj["title"])
                plt.xlabel(obj["xlabel"])
                plt.ylabel(obj["ylabel"])
                plt.plot(arrayX, arrayY)
                plt.show()


def SaveImage(obj, path='/'):
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
            plt.title(obj["title"])
            plt.xlabel(obj["xlabel"])
            plt.ylabel(obj["ylabel"])
            plt.plot(arrayX, arrayY)
            plt.savefig(path+obj["title"] + ".png")
