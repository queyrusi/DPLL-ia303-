IA303 : DPLL SAT solver and Tseytin Transform implementation
====

### Authors
Zhi Zhou, <zhi.zhou@ensta-paris.fr>
 Simon Queyrut,  <simon.queyrut@ensta-paris.fr>
 
 [@zroykhi](https://github.com/zroykhi), [@queyrusi][github] 

[github]: http://github.com/queyrusi


## Content
+ `simple_dpll.py` with DPLL funciton and its `propagate` function below
+ `tseitin_recursive.py` and `tseitin_iterative.py` implement two *different methods* of Tseytin transform
+ `cnf_files` contains `.cnf` files in DIMACS format

## Usage 

+ If you already have DIMACS CNF file, simply run
```bash
python sat_solve.py file.cnf
```
but if you don't, feel free to use examples on which we already tested or small solver (*careful*: some extremely large DIMACS can take several minutes to solve):
```bash
python sat_solve.py ./cnf_files/SAT/simple.cnf
```
**Note**: it wont return anything if UNSAT.

-------------


+ Or you could **use your own formula**:

1. Try to ransform a string of logic formula into cnf using Tseitin tranformation:
```
python tseitin_recursive.py --logic '!(p|q|s|t)&z'
```
result will be like `~p&~q&~s&s0&~s2&~s3&~s4&~t&z`. You can also use `tseitin_iterative.py` if you feel like it.


2. If you want to solve, run all these commands in a pipeline:
```
python tseitin_recursive.py --logic '!(p|q|s|t)&z' | python parsercnf2dimacs.py | python simple_dpll.py
```
It will give an output like 
`[+] SAT` and `[-1, 9, -6, -5, -3, -8, -4, -7, 2]` which is the model for Tseitin transformation (hence higher number of variables).

