import boolean

algebra = boolean.BooleanAlgebra()
TRUE, FALSE, NOT, AND, OR, symbol = algebra.definition()

def Tseitin_recurrent(formula, counter, var_base):
    """Tseitin transformation
    :param formula: <class 'boolean.boolean'> 
    :param var_base: A string used to create new variable without being conflict with the existing variables.
    """
    # global counter, var_base
    if formula.isliteral:
        return (formula, TRUE)
    else:
        args = formula.args
        f1 = args[0]
        p = str(var_base) + str(counter)
        p = algebra.Symbol(p)        
        counter = counter + 1
        if formula.operator == '~':
            p0, c0 = Tseitin_recurrent(f1, counter, var_base)
            return (NOT(p0), c0)
        elif formula.operator == '|':
            f2 = OR(*args[1:len(args)]) if (len(args) > 2) else args[1]
            p1, c1 = Tseitin_recurrent(f1, counter, var_base)
            p2, c2 = Tseitin_recurrent(f2, counter, var_base)        
            return (p, (AND(OR(NOT(p), p1, p2), OR(p, NOT(p1)), OR(p, NOT(p2)), c1, c2)).simplify())    
        elif formula.operator == '&':
            f2 = AND(*args[1:len(args)]) if (len(args) > 2) else args[1]
            p1, c1 = Tseitin_recurrent(f1, counter, var_base)
            p2, c2 = Tseitin_recurrent(f2, counter, var_base)            
            return (p, (AND(OR(p, NOT(p1), NOT(p2)), OR(NOT(p), p1), OR(NOT(p), p2), c1, c2).simplify()))


if __name__ == "__main__":
    a = "!(p|q|s|t)&!r"

    f = algebra.parse(a)

    counter = 0
    var_base = next(iter(f.symbols))
    p, c = Tseitin_recurrent(f, counter, var_base)
    cnf_formula = AND(p, c).simplify()
    print('After Tseitin transformation: {}'.format(cnf_formula))          