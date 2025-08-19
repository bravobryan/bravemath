# from bravemath.stat_functions.linreg import linear_regression
# from bravemath.stat_functions.evaluate import rmse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import seaborn as sns


number_range = [*range(1, 100)]
df = pd.DataFrame({
    "char_col": [f"TheNumber-{i}" for i in number_range],
    "int_col": [f"  {i}   " for i in range(100, len(number_range)+100)],
    "random_int": np.random.randint(1,5, size=len(number_range))
})

df2 = pd.DataFrame()
df2['char_num'] = df['char_col'].str.extract('(\d+)').astype(int)
df2['int_num'] = df['int_col'].str.strip().astype(int)
df2['letter'] = df['random_int'].replace({1: 'A', 2: 'B', 3: 'C', 4: 'D'})

# df.to_csv('test.csv', index=False)
# df2.to_csv('test2.csv', index=False)