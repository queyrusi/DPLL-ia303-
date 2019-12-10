import sys

filename = sys.argv[1]

def read_file_to_list(filename):
    with open(filename,"r") as dimacs:
        lines = dimacs.readlines()
        lines = [l.replace('\n', '').split() for l in lines]
        clauses = []
        tmp = None
        for line in lines:
            if tmp is not None:
                line = tmp + line
                tmp = None
            if line[0] != 'c' and line[0] != 'p' and line[-1] != '0':
                tmp = line
            else:
                clauses.append(line)
        return clauses

def DIMACSParser(lines):
    F_str = [item[0:-1] for item in lines if (('c' not in item) and ('p' not in item))]
    F = []
    clause = []
    for str_clause in F_str:
        for literal in str_clause:
            clause.append(int(literal))
        F.append(clause)
        clause = []
    return F

if __name__ == "__main__":
    lines = read_file_to_list(filename)
    f = DIMACSParser(lines)
    print(f)
