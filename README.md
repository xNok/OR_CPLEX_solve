CPLEX SOLVE
---

This Python library provide a simplified way to use the CPLEX Python API. In other words, it provides a funtion that helps you formulate your linear programs.

# Matrix methods

Solve a linear program with the form $$ \{ c x : A x \le b \} $$

```Python
from_matrices(c,A,B,
    relaxation=True,path=None,verbose=False,minimize=True,senses="L")
```

Parameters:
    * relaxation=False => Solve the Integer linear programs
    * path="mylp.lp"   => When specified output the OPL formulation
    * verbose=True     => Display CPLEX logs
    * minimize=True    => Set to minimisation problem
    * sense="L"        => Sense of inequation constraint ( "L" less, "G" greater, "E" Equal)

# More complex formulation

Solve a linear problem by providing a set of constraint and decision variables.

```Python
from_template(variables,constraints,
    minimize=True, path=None, verbose=False)
```

Each set of variables can be describe as following:

```Python
Xs = {
    "name" : [X(i) for i in I],
    "coef" : [c[i] for i],
    "type" : ["C" if relaxation else "I" for i in I],
    "ub"   : [1 for i in I],
    "lb"   : [0 for i in I],
}

[...]

variables = [Xs, ...]
```

Each set of constraint can be defined as following:

```Python
c1 = {
    "lin_expr": [[[
    # Decision variables
    ], [
    # Associated Coefficient
    ]] for i in I],
    "senses"  : ["L" for i in I],
    "rhs"     : [ 0  for i in I]
}

constraints = [c1]
```

You can use `0_template.ipynb` as a starting point.

Several example are availiable at [Location-routing-problems](https://github.com/xNok/OR_location_routing_problem_study)
