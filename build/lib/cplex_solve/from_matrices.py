
from cplex_solve.from_template import from_template

def from_matrices(c,A,B,relaxation=False,path=None,verbose=False,minimize=True,senses="L"):
    """
    c   coefficent of the objective function
    A   coefficent of the constaints
    B   Right-hand-side
    """
    #####################################################################
    # Decision variables
    
    def X(i):
        return "X_" + str(i)
    
    I = range(len(c)); J = range(len(B))
    #####################################################################
    # Objective function
    
    Xs = {
        "name" : [X(i) for i in I],
        "coef" : c,
        "type" : ["C" if relaxation else "I" for i in I],
        "ub"   : [],
        "lb"   : [0 for i in I],
    }

    variables = [Xs]
    #####################################################################
    # Constraints
    
    c1 = {
        "lin_expr": [[[X(i) for i in I], A[j]]
                     for j in J],
        "senses"  : [senses for j in J],
        "rhs"     : B
    }
    
    constraints = [c1]
    #####################################################################
    # Solving
    prob = from_template(variables,constraints,
                       minimize=minimize, path=path, verbose=verbose)

    return prob