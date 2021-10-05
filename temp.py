from math import ceil

import pandas as pd

"""
import pandas as pd
df=pd.read_csv('/home/shubham/Documents/prachi/bhaskar.csv')
l1=ceil(len(df)/4)
df1=df[:l1]
df2=df[l1:2*l1]
df3=df[2*l1:3*l1]
df4=df[3*l1:]
df1.to_csv('/home/shubham/Documents/prachi/bhaskar1.csv')
df2.to_csv('/home/shubham/Documents/prachi/bhaskar2.csv')
df3.to_csv('/home/shubham/Documents/prachi/bhaskar3.csv')
df4.to_csv('/home/shubham/Documents/prachi/bhaskar4.csv')
"""

df=pd.read_csv('/home/shubham/Documents/prachi/bhaskar.csv')

df1=pd.read_csv('/home/shubham/Documents/prachi/bhaskar1.csv')
df2=pd.read_csv('/home/shubham/Documents/prachi/bhaskar2.csv')
df3=pd.read_csv('/home/shubham/Documents/prachi/bhaskar3.csv')
df4=pd.read_csv('/home/shubham/Documents/prachi/bhaskar4.csv')

print(len(df1)+len(df2)+len(df3)+len(df4))

print(len(df))