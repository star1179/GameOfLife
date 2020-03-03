import sys

class App():

    def __init__(self, ag):
        self.ag = ag

    def initState(self):
        if len(self.ag) > 1:
            try:
                fd = open(self.ag[1],"r")

            except FileNotFoundError:
                pass

            else:
                lines = fd.readlines()
                self.width = lines[0]
                self.height = lines[1]


if __name__ == "__main__":
    ag = sys.argv
