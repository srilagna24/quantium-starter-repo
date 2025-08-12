import pandas as pd
from dash import Dash, html, dcc, Input, Output

# Load the combined and cleaned sales data
df = pd.read_csv('pink_morsel_sales.csv')

# Convert the 'date' column to datetime to ensure proper sorting
df['date'] = pd.to_datetime(df['date'])

# Create a Dash app instance
app = Dash(__name__)

# Define the app's layout with CSS styling
app.layout = html.Div(style={'backgroundColor': '#f8f9fa', 'fontFamily': 'Arial'}, children=[
    html.H1(children='Pink Morsel Sales Analysis', style={'textAlign': 'center', 'color': '#007bff', 'paddingTop': '20px'}),

    html.Div(children=[
        html.H3(children='Select a Region:', style={'marginRight': '10px'}),
        dcc.RadioItems(
            id='region-radio',
            options=[
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
                {'label': 'All', 'value': 'all'}
            ],
            value='all',  # Default selected value
            inline=True,
            style={'display': 'flex', 'alignItems': 'center', 'justifyContent': 'center'}
        ),
    ], style={'display': 'flex', 'alignItems': 'center', 'justifyContent': 'center', 'marginBottom': '20px'}),

    dcc.Graph(id='sales-line-chart'),
])

# Define a callback to update the chart based on the radio button selection
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-radio', 'value')
)
def update_graph(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]

    # Create the figure with the filtered data
    fig = {
        'data': [
            {'x': filtered_df['date'], 'y': filtered_df['sales'], 'type': 'line', 'name': 'Pink Morsel Sales'}
        ],
        'layout': {
            'title': f'Daily Sales of Pink Morsels in the {selected_region.capitalize()} Region',
            'xaxis': {'title': 'Date'},
            'yaxis': {'title': 'Sales ($)'}
        }
    }
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)