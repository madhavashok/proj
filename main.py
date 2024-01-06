import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

data = {
    'Temperature': [300, 500, 700, 900, 1100],
    '1/2<110>': [0.000216129, 8.68509E-05, 3.31636E-05, 2.63173E-06, 4.8687E-06],
    '1/3<100>': [0.000109687, 4.86776E-05, 1.3765E-05, 1.27846E-06, 1.34299E-06],
    '1/3<111>': [1.36184E-05, 5.18985E-06, 8.53197E-07, 2.65589E-07, 2.2607E-07],
    '1/6<110>': [3.43614E-05, 2.3915E-05, 6.8998E-06, 1.20263E-06, 2.26828E-06],
    '<1/6<112>': [0.008984957, 0.001017106, 0.000331677, 3.66592E-05, 5.9763E-05],
    'AVG': [0.00187175, 0.000236348, 7.72717E-05, 8.40751E-06, 1.36938E-05]
}

df = pd.DataFrame(data)

regression_line_temp_vs_density = px.scatter(df, x='Temperature', y='AVG', trendline='ols').data[1]

app = dash.Dash(__name__)

material_description = """

316SS data by Abhishek CR 

316 Stainless Steel, a popular stainless steel alloy, is composed of 24% Nickel (Ni), 17% Chromium (Cr), and 59% Iron (Fe). 
This specific composition imparts excellent corrosion resistance, making it suitable for a wide range of applications, 
especially in harsh environments. The combination of Nickel and Chromium enhances the alloy's resistance to corrosion 
and oxidation, while the majority Iron content provides structural strength. 316 Stainless Steel is widely used in 
various industries, including marine, chemical, and medical, due to its superior corrosion resistance, durability, 
and versatility.
"""

app.layout = html.Div([
    html.P(material_description),
    dcc.Graph(
        id='bar-graph',
        figure=px.bar(df, x='Temperature', y=df.columns[1:], title='Dislocation Density for Different Categories')
    ),
    dcc.Graph(
        id='linear-regression',
        figure=px.scatter(df, x='Temperature', y='AVG', title='Linear Regression: Temperature vs. Dislocation Density')
            .add_trace(regression_line_temp_vs_density)
    ),
])

if __name__ == '__main__':
    app.run_server(debug=True)
