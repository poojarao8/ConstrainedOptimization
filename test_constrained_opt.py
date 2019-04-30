#source:https://stackoverflow.com/questions/13670333/multiple-variables-in-scipys-optimize-minimize
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html#scipy.optimize.minimize

import scipy.optimize as optimize
import numpy as np

def f(params):
    #print(params)  # <-- you'll see that params is a NumPy array
    m, a = params # <-- for readability, assign names to component variables
    return 6.0*m**3 - 4.0*(a+1)**3 - 12.0

def constraint(x):
    pass
    # replace this with my constraints
    # not using this at the moment
    # but probably a better way to put in the constraints
    #return np.atleast_1d(np.sum(np.abs(x)))


initial_guess = [23, 19] 
# x = [m, a], so x[0] is m and x[1] is a
result = optimize.minimize(f, initial_guess, 
         constraints=({"type": "ineq",  
                       "fun": lambda x: x[0]**3 - ((3.0/2.0)*(x[1]*x[1]+3.0*x[1])+9.0)*x[0]
                                       + 2.0/3.0*(x[1]**3+3.0*x[1]*x[1]+2.0*x[1])},
                      {"type": "ineq",
                       "fun": lambda x: x[1]*(x[1]+1.0)*(x[0]/x[1]*3.0-2.0) - 4.0}),
         bounds=((1,None),(1,None)), options=dict({'maxiter': 20})
                          )

if result.success:
    fitted_params = result.x
    print(fitted_params)
else:
    raise ValueError(result.message)


