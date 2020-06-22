import plotly.graph_objects as pgo
import plotly.express as px
import pandas as pd

import excel_read as xr

wide_df = pd.DataFrame(xr.ngames_by_platform_and_year())
df = wide_df.melt(id_vars="Year")

fig = px.scatter(df, x="Year", y="value", color="variable")
fig.show()
