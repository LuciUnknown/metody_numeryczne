
def read_coefficient(path):
    table  = []
    with open(path) as f:
        while True:
            aftertable = []
            line = f.readline()
            if line == '':
                return table

            row = line.split(' ')
            for i in row:
                aftertable.append(float(i))
            table.append(aftertable)