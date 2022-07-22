import pip as pip


class packageManager:

    def install(*package):
        for pace in package:
            print("installing " + pace + "...")
            pip.main(["install", pace])
        print("you are good to Go!")
