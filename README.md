IA303 : DPLL SAT solver and Tseytin Transform implementation
====

### Authors
Zhi Zhou, <zhi.zhou@ensta-paris.fr>
 Simon Queyrut,  <simon.queyrut@ensta-paris.fr>
 
 [@zroykhi](https://github.com/zroykhi), [@queyrusi][github] 

[github]: http://github.com/queyrusi


## Content
+ `simple_dpll.py` with DPLL funciton and its `propagate` function below
+ `tseytin_recursive.py` and `tseytin_iterative.py` implement Tseytin transform
+ `cnf_files` contains `.cnf` files in DIMACS format

### Usage 

1. Transform a string of logic formule into cnf using Tseitin tranformation:
```
python tseitin_recursive.py --logic '!(p|q|s|t)&z'
```
result will be like `~p&~q&~s&s0&~s2&~s3&~s4&~t&z`

2. Parse cnf in string to a list of DIMACS format
```
python parsercnf2dimacs.py
```
then enter your cnf in the terminal, for example, `~p&~q&~s&s0&~s2&~s3&~s4&~t&z`. It will output the result like `[[-7], [-1], [-4], [2], [-8], [-6], [-5], [-3], [9]]`

3. Find model using dpll
```
python simple_dpll.py
```
then enter your dimacs list, like `[[-7], [-1], [-4], [2], [-8], [-6], [-5], [-3], [9]]`. It will output the result, like `[-7, -1, -4, 2, -8, -6, -5, -3, 9]`

4. Or you can run all these commands in a pipeline:
```
python tseitin_recursive.py --logic '!(p|q|s|t)&z' | python parsercnf2dimacs.py | python simple_dpll.py
```

5. Read a DIMACS file and transform to a list
```
python dimacs_parser.py --file cnf_files/simple.cnf
```
It will give an output like `[[1, 2], [2, -3, 4], [-1, -2], [-1, 3, -4], [1]]`

6. Read a DIMACS file and use dpll to output the result
```
python dimacs_parser.py --file cnf_files/simple.cnf | python simple_dpll.py
```
It will give an output like `[1, -2, -3, -4]`