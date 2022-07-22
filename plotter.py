
try:
    import matplotlib.pyplot as plt
except ImportError:
    from packageManager import packageManager as packMan
    packMan.install("matplotlib")
    import matplotlib.pyplot as plt


def plot(obj):
    if obj["type"] == "numarray":
        plt.plot(obj["x"], obj["y"])
        plt.xlabel(obj["xlabel"])
        plt.ylabel(obj["ylabel"])
        plt.title(obj["title"])
        plt.show()


print("☺️")
