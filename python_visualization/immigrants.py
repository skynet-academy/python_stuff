import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df_canada = pd.read_excel('./Canada.xlsx', sheet_name="Canada by Citizenship", skiprows=20)
df_canada.sort_values(['Total'], ascending= False, axis= 0, implace= True)

plt.show()

