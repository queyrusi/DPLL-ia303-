import boolean
from DIMACSParser import DIMACSParser
from boolean.boolean import *
from ParserFormuleToDimacs import *
from Tseitin_recurrent  import Tseitin_recurrent

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
    var_base = next(iter(formule_in_boolean.symbols))
    p, c = Tseitin_recurrent(formule_in_boolean, 0, var_base)
    cnf_in_boolean = AND(p, c).simplify()
    # cnf_in_boolean = algebra.cnf(formule_in_boolean)
    dimacs = ParserCNF2Dimacs(cnf_in_boolean.__str__())  
    print(dimacs)
    aa = DIMACSParser(dimacs)
    print(aa)