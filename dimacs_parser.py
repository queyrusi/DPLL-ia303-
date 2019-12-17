import argparse

def read_file_to_list(filename):
    """Read a dimacs file to a list
    Args:
        file: str
            file name
    Returns
    -------
        clauses: list
            list of clause
    """
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

def dimacs_parser(lines):
    """extrait clauses and variables from dimacs format
    Args:
        lines: list
            dimacs content in a list

    Returns
    -------
        F: list
            clauses and variables in a list
    """
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
    parser = argparse.ArgumentParser(description="Read a cnf file and transform to a list")
    parser.add_argument('--file', help="cnf file path", default="cnf_files/simple.cnf", type=str)
    args = parser.parse_args()
    lines = read_file_to_list(args.file)
    f = dimacs_parser(lines)
    print(f)
