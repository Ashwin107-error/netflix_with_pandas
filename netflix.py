import pandas as pd
import plotly.express as px

df = pd.read_csv('netflix_titles.csv')
df.drop(['duration','description','date_added'],axis=1,inplace=True)
df.drop_duplicates(inplace=True)
# creating pie chart for all ratings of all the contents
movies = df.groupby(['rating']).size().reset_index(name='counts')
piechart = px.pie(movies,values='counts',names='rating',title='Content Rating Distribution in Netflix')
piechart.show()

# filtering out all the cast members
filtered_actors = df['cast'].str.split(',',expand=True).stack()
filtered_actors=filtered_actors.to_frame()
filtered_actors.columns = ['Cast']
actors = filtered_actors.groupby(['Cast']).size().reset_index(name='Total Content')
actors = actors['No Data' != actors.Cast]

actors = actors.sort_values(by=['Total Content'],ascending=False)
top5 = actors.head()
top5 = top5.sort_values(by=['Total Content'])

bar = px.bar(top5,x='Total Content',y='Cast',title='Top 5 Actors on Netflix',color=['blue','green','pink','black','yellow'])
bar.show()

# Analyze the trend in production

df_one = df[['type','release_year']]
df_one = df_one.rename(columns={'release_year':"Release Year"})

production_data = df_one.groupby(['Release Year','type']).size().reset_index(name = 'Total Content')
production_data = production_data[production_data['Release Year']>2012]
chart = px.line(production_data, x="Release Year", y="Total Content", color='type',title='Trend of content produced over the years on Netflix')
chart.show()

# To find a reality show suitable for kids below 14

df.drop(['cast', 'director', 'type', 'show_id', 'country', 'release_year'],axis=1,inplace=True) # remove unwanted columns for better visual result
df.drop_duplicates(inplace=True)
reality_shows = df.loc[(df['listed_in']=='Reality TV') & (df['rating']== 'TV-14')] #locating reality tv and tv-14 from both listed in and rating respectively

pd.set_option('display.max_rows',None)
print(reality_shows) #Accordingly, we can use the same code for filtering any other type of content. For example, if we want to filter the TV shows suitable for children under the age of 6, we can use the following format.







