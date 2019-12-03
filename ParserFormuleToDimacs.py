import boolean
from DIMACSParser import DIMACSParser

def ParserFormuleToDimacs(formule):
    """formule: <class 'boolean.boolean'>"""
    cnf_str = str(algebra.cnf(formule))
    all_alpha = "".join(filter(str.isalpha, cnf_str))
    uniq_alpha = list(set([i for i in all_alpha]))
    uniq_alpha = sorted(uniq_alpha)
    cluste_list = cnf_str.split('&')
    num_cluste = len(cluste_list)

    dimacs = ['c this is a simple dimacs'.split(), 'c this is a comment 0'.split()]
    dimacs.append("p cnf {} {}".format(len(uniq_alpha), num_cluste).split())
    for i in range(num_cluste):
        f = cluste_list[i]
        element_list = f.replace('(', '').replace(')', '').split('|')
        mid_f = []
        for ele in element_list:
            if ele.startswith('~'):
                mid_f.append(-(uniq_alpha.index(ele.replace('~', ''))+1))
            else:
                mid_f.append(uniq_alpha.index(ele)+1)
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
    formule = str_to_formule(formule_in_string)    
    dimacs = ParserFormuleToDimacs(formule)  
    print(dimacs)
    aa = DIMACSParser(dimacs)
    print(aa)


