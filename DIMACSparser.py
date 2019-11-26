filename = "simple.cnf"

def DIMACSParser(filename):
    with open(filename,"r") as dimacs:
        lines = dimacs.readlines()
        F = []
        lines = [l.replace('\n', '').split() for l in lines]
        start_flag = False
        num_clause = 0
        for line in lines:
            if line[0] == 'p':
                start_flag = True
                num_clause = int(line[-1])
            # don't count a comment row ends with 0, number of clause must be consistant
            if line[-1] == '0' and start_flag and len(F) < num_clause:
                tmp = {}
                for i in range(len(line) - 1):
                    tmp[int(line[i])] = None
                F.append(tmp)
        return F

if __name__ == "__main__":
    f = DIMACSParser(filename)
    print(f)