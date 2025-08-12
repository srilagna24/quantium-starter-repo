import pandas as pd
from dash import Dash, html, dcc

# Load the combined and cleaned sales data
df = pd.read_csv('pink_morsel_sales.csv')

# Convert the 'date' column to datetime to ensure proper sorting
df['date'] = pd.to_datetime(df['date'])

# Create a Dash app instance
app = Dash(__name__)

# Define the app's layout
app.layout = html.Div(children=[
    html.H1(children='Pink Morsel Sales Analysis'),

    dcc.Graph(
        id='sales-line-chart',
        figure={
            'data': [
                {'x': df['date'], 'y': df['sales'], 'type': 'line', 'name': 'Pink Morsel Sales'}
            ],
            'layout': {
                'title': 'Daily Sales of Pink Morsels',
                'xaxis': {'title': 'Date'},
                'yaxis': {'title': 'Sales ($)'}
            }
        }
    )
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)