import pandas as pd
import plotly.figure_factory as ff
import scipy

df = pd.read_csv("data.csv")
# mean = df["Avg Rating"].mean()

fig = ff.create_distplot([df["Avg Rating"].tolist()], ["Average Rating"], show_hist=False)
fig.show()
