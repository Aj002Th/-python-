class Fileobject:
    def __init__(self, file):
        self.file = open(file)

    def __del__(self):
        self.file.close()
        del self.file
