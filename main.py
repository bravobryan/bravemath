from bravemath.stat_functions.linreg import LinearRegression

x = [1, 2, 2, 3]
y = [1, 2, 3, 6]

linreg = LinearRegression().fit(x, y)
print(linreg.model)