import random
import pandas as pd

SQL="select * from 'ba820.datasets.mtcars"
PROJECT='ba820'

df=pd.read_gbq(SQL,PROJECT)


