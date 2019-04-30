#source:https://stackoverflow.com/questions/13670333/multiple-variables-in-scipys-optimize-minimize
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html#scipy.optimize.minimize

import scipy.optimize as optimize
import numpy as np

def f(params):
    #print(params)  # <-- you'll see that params is a NumPy array
    m, a = params # <-- for readability, assign names to component variables
    return 6.0*m**3 - 4.0*(a+1)**3 - 12.0

def constraint(x):
    # replace this with my constraints
    # PRAO: not sure how to do this part
    return np.atleast_1d(np.sum(np.abs(x)))


initial_guess = [1, 1]
# I think I can use bounds for enforcing the positivity requirement on m and a
# not sure if I am doing this right though
bnds = ((0,None), (0, None)) # tuple for 1d box constraint
#result = optimize.minimize(f, initial_guess, constraints={"fun": constraint, "type": "ineq"})
result = optimize.minimize(f, initial_guess, bounds=bnds, constraints={"fun": constraint, "type": "ineq"})

if result.success:
    fitted_params = result.x
    print(fitted_params)
else:
    raise ValueError(result.message)


