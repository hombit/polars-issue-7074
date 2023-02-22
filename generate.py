import numpy as np
import polars as pl

rng = np.random.default_rng(0)
n_cols = 304
n_rows = 4053955

df = pl.DataFrame({f'c{i:03d}': np.zeros(n_rows) for i in range(n_cols)})
df.write_csv('test.csv.bz2')