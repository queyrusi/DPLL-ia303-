import boolean
from dimacs_parser import dimacs_parser
from boolean.boolean import *
from parsercnf2dimacs import *
from tseitin_recursive  import tseitin_recursive

if __name__ == "__main__":
    a = 'x | !y & (z | t)'
    # a = '!y & (z | t)'
    # a = '!y | (z | t)'
    # a = '!y'
    # a = '!(x&y)'
    # a = '!(x|y)'
    # a = '(x|y)&(ee|f)'
    # a = '~(x|y)&(ee|f)'
    # a = '~(x|y)' 
    # a = 'y'
    a = "!(a&b)|(c&(d&e))|(!f&(g&!h))"
    a = "!(p|q|s|t)&!r"    
    algebra = boolean.BooleanAlgebra()
    # change your formule string here
    formule_in_string = 'x | !y & (z | t) '
    formule_in_boolean = str_to_formule(formule_in_string)    
    cnf_in_boolean = tseitin_recursive(formule_in_boolean)
    # cnf_in_boolean = algebra.cnf(formule_in_boolean)
    dimacs = parsercnf2dimacs(cnf_in_boolean.__str__())  
    print(dimacs)
    aa = dimacs_parser(dimacs)
    print(aa)