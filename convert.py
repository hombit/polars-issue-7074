import polars
polars.scan_csv(
    'test.csv.bz',
    rechunk=False
).sink_parquet('test.parquet', row_group_size=1<<12, maintain_order=False)