filename = "simple.cnf"
with open(filename,"r") as dimacs:
    data = dimacs.readlines()
    F = []
    for element in data:
        element.replace('\n', '')
    for element in data:
        if element.startswith('p'):
            for k in range(int(element[-1])):
                F.append(dict())

# must return F = [{'1':None, '-3':None},{...} ]