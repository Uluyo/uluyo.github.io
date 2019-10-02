
import plotly_express as px

gapminder = px.data.gapminder()
fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
                 hover_name="country", log_x=True, size_max=60)
fig.show()

import chart_studio.tools as tls
tls.get_embed('https://uluyo.github.io') 