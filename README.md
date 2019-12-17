# DPLL-ia303-

transform a string of logic formule into cnf using Tseitin tranformation:
```
python Tseitin_recursive.py --logic '!(p|q|s|t)&z'
```
result will be like `~p&~q&~s&s0&~s2&~s3&~s4&~t&z`

Parse cnf in string to a list of DIMACS format
```
python ParserCNF2Dimacs.py
```
then enter your cnf in the terminal, for example, `~p&~q&~s&s0&~s2&~s3&~s4&~t&z`. It will output the result like `[[-7], [-1], [-4], [2], [-8], [-6], [-5], [-3], [9]]`

find model using dpll
```
python simple_dpll.py
```
then enter your dimacs list, like `[[-7], [-1], [-4], [2], [-8], [-6], [-5], [-3], [9]]`. It will output the result, like `[-5, -2, -6, 4, -9, -3, -7, -8, 1]`

Or you can run all these command in a pipeline:
```
python Tseitin_recursive.py --logic '!(p|q|s|t)&z' | python ParserCNF2Dimacs.py | python simple_dpll.py
```