from __future__ import print_function
import numpy as np
import pandas as pd
df_can = pd.read_excel('./Canada.xlsx', sheet_name="Canada by Citizenship", skiprows=range(20), skipfooter=2)
df_can.head()
