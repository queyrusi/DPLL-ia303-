import boolean
from dimacs_parser import dimacs_parser
from boolean.boolean import *
import argparse
import sys

def parsercnf2dimacs(cnf_str):
    """Parse cnf in string to DIMACS format
    Args:
        cnf_str : string
            a string of cnf
            
    Returns
    -------
        dimacs : list of lists
            dimacs format
    """
    algebra = boolean.BooleanAlgebra()
    logic_formule = algebra.parse(cnf_str)
    variables = logic_formule.symbols
    variables = list(map(str, variables))

    cluste_list = cnf_str.split('&')
    num_cluste = len(cluste_list)

    dimacs = ['c this is a simple dimacs'.split(), 'c this is a comment 0'.split()]
    dimacs.append("p cnf {} {}".format(len(variables), num_cluste).split())
    for i in range(num_cluste):
        f = cluste_list[i]
        element_list = f.replace('(', '').replace(')', '').split('|')
        mid_f = []
        for ele in element_list:
            if ele.startswith('~'):
                mid_f.append(-(variables.index(ele.replace('~', ''))+1))
            else:
                mid_f.append(variables.index(ele)+1)
        mid_f.append(0)
        dimacs.append(mid_f)
    return dimacs

def str_to_formule(formule_in_string):
    algebra = boolean.BooleanAlgebra()
    return algebra.parse(formule_in_string)       


if __name__ == "__main__":
    algebra = boolean.BooleanAlgebra()
    # change your formule string here
    formule_in_string = 'x | !y & (z | t) '
    try:
        formule_in_string = sys.stdin.readline()
    except Exception as e:
        print('Error', e)            

    formule_in_boolean = str_to_formule(formule_in_string)    
    cnf_in_boolean = algebra.cnf(formule_in_boolean)
    dimacs = parsercnf2dimacs(cnf_in_boolean.__str__())  
    aa = dimacs_parser(dimacs)
    print(aa)


