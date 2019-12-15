import boolean
from DIMACSParser import DIMACSParser
from boolean.boolean import *
from ParserFormuleToDimacs import *
from Tseitin_recursive  import Tseitin_recursive

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
    cnf_in_boolean = Tseitin_recursive(formule_in_boolean)
    # cnf_in_boolean = algebra.cnf(formule_in_boolean)
    dimacs = ParserCNF2Dimacs(cnf_in_boolean.__str__())  
    print(dimacs)
    aa = DIMACSParser(dimacs)
    print(aa)