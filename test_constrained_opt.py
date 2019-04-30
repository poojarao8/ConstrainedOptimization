# References: 
# https://stackoverflow.com/questions/13670333/multiple-variables-in-scipys-optimize-minimize
# https://www.youtube.com/watch?time_continue=5&v=cXHvC_FGx24
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html#scipy.optimize.minimize

import scipy.optimize as optimize
import numpy as np

# first define an objective function
def objective(x):
    m = x[0] 
    a = x[1]
    return 6.0*m**3 - 4.0*(a+1)**3 - 12.0

# then define the constraints
def constraint1(x):
    m = x[0]
    a = x[1]
    return m**3 - ((3.0/2.0)*(a*a+3.0*a)+9.0)*m + 2.0/3.0*(a**3+3.0*a*a+2.0*a) 

def constraint2(x):
    m = x[0]
    a = x[1]
    return a*(a+1.0)*(m/a*3.0-2.0) - 4.0

# positivity of m and a is enforced via using "bounds", which are bounded below by 1
# these bounds however do not guarantee that m and a will be integers
# they take them to be reals >= 1

initial_guess = [23, 20] 

result = optimize.minimize(
         objective, 
         initial_guess, 
         constraints=({"type": "ineq", "fun": constraint1},  
                      {"type": "ineq", "fun": constraint2}),
         bounds=((1,None),(1,None)), # these are not integer bounds 
         options=dict({'maxiter': 20})
                          )

if result.success:
    fitted_params = result.x
    print(fitted_params)
else:
    raise ValueError(result.message)


