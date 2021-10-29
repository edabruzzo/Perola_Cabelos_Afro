from dash import html
from dash import dcc
from dash import html


class Layout(object):


    theme = {
        "accent": "#2BFEBE",
        "accent_negative": "#ff2c6d",
        "accent_positive": "#33ffe6",
        "background_content": "#1D262F",
        "background_page": "#242e3f",
        "border": "#5C8CBE",
        "border_style": {
            "name": "underlined",
            "borderTopWidth": 0,
            "borderRightWidth": 0,
            "borderLeftWidth": 0,
            "borderBottomWidth": "1px",
            "borderBottomStyle": "solid",
            "borderRadius": 0,
            "inputFocus": {
                "outline": "transparent"
            }
        },
        "breakpoint_font": "1200px",
        "breakpoint_stack_blocks": "700px",
        "colorway": [
            "#2bfebe",
            "#4c78a8",
            "#f58518",
            "#e45756",
            "#54a24b",
            "#eeca3b",
            "#b279a2",
            "#ff9da6",
            "#9d755d",
            "#bab0ac"
        ],
        "colorscale": [
            "#2bfebe",
            "#27e8aa",
            "#22d396",
            "#1ebd83",
            "#19a971",
            "#14945f",
            "#0f814d",
            "#096e3c",
            "#045b2b",
            "#00491b"
        ],
        "font_family": "Ubuntu",
        "font_size": "17px",
        "font_size_smaller_screen": "15px",
        "font_family_header": "Playfair",
        "font_size_header": "24px",
        "font_family_headings": "Playfair",
        "text": "#87B4E5",
        "report_font_family": "Ubuntu",
        "report_font_size": "12px",
        "report_background_page": "white",
        "report_background_content": "#FAFBFC",
        "report_text": "black"
    }


    def definir_layout_aplicacao(self, app, df):

        app.layout = html.Div([
            dcc.Graph(id='graph-with-slider'),
            dcc.Slider(
                id='year-slider',
                min=df['year'].min(),
                max=df['year'].max(),
                value=df['year'].min(),
                marks={str(year): str(year) for year in df['year'].unique()},
                step=None
            )
        ])

        return app
