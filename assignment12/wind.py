import plotly.express as px
import plotly.data as pldata

df = pldata.wind(return_type = 'pandas')

print(df.head(10))
print(df.tail(10))

df['strength'] = df['strength'].str.replace(r'\D', '', regex = True).astype(float)

fig = px.scatter(df, x = 'frequency', y = 'strength', color = 'direction', 
                 title = 'strength vs. frequency', hover_data = ['direction'])

fig.write_html('wind.html')