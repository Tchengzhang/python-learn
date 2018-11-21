#绘制股票走势图
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['font.family'] = 'STSong'

df = pd.read_csv("f://all_stock_data/600001_20181001.csv",encoding="gbk")
print(df.head(2))
df.plot()

