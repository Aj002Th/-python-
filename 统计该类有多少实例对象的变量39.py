class CC:
    count = 0

    def __init__(self):
        CC.count += 1

    def __del__(self):
        CC.count += 1