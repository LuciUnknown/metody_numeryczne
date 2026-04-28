

def read(path):
    x = []
    with open(path) as f:
        array = f.readline().split(',')
        for i in array:
            x.append(float(i))

        return x