"""
Separate the app definiton from the app startup program (main.py).
This allows the app to be imported into the component modules where
callbacks are registered. This pattern will prevent circular imports
on startup.
"""

from dash import Dash

app = Dash(__name__)
