
import cplex
import cplex_solve

def from_template(variables,constraints, minimize=True, path=None, verbose=False):
    
    #####################################################################
    # Extract variables
    obj, ub, lb, colnames, types = cplex_solve.from_template_extract_variables(variables)
    #####################################################################
    # Extract constraints
    rows, senses, rhs = cplex_solve.from_template_extract_constraints(constraints)
    #####################################################################
    # Creating problem
    prob = cplex.Cplex()
    
    #Disable logging
    if not verbose:
        prob.set_log_stream(None)
        prob.set_error_stream(None)
        prob.set_warning_stream(None)
        prob.set_results_stream(None)
    
    ## Objective function sense
    if minimize:
        prob.objective.set_sense(prob.objective.sense.minimize)
    else:
        prob.objective.set_sense(prob.objective.sense.maximize)
    ## Objective function
    prob.variables.add(obj=obj,ub=ub,lb=lb,names=colnames,types=types)
    ## Constraintes
    prob.linear_constraints.add(lin_expr=rows,senses=senses, rhs=rhs)

    #####################################################################
    # Saving the linear problem formulation into a file
    if path:
        prob.write(path) # print the formulation into a file

    #####################################################################
    # Solving problem
    prob.solve()
    
    return prob