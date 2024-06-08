from bravemath.stat_functions.linreg import linear_regression

x = [1, 2, 2, 3]
y = [1, 2, 3, 6]

linreg = linear_regression().fit(x, y)
print(linreg.model)