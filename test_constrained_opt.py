#source:https://stackoverflow.com/questions/13670333/multiple-variables-in-scipys-optimize-minimize
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html#scipy.optimize.minimize

import scipy.optimize as optimize

def f(params):
    # print(params)  # <-- you'll see that params is a NumPy array
    a, b, c = params # <-- for readability you may wish to assign names to the component variables
    return a**2 + b**2 + c**2

initial_guess = [1, 1, 1]
result = optimize.minimize(f, initial_guess)
if result.success:
    fitted_params = result.x
    print(fitted_params)
else:
    raise ValueError(result.message)


# PRAO: my initial goal is to optimize a function that looks like
# 6m^3 - 4(a+1)^3, where a and b are positive integers
# There is two other inequalities that are constraints, but not bothered about themat the moment

