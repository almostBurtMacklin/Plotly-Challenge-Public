import dash
#from scout_apm.flask import ScoutApm

app = dash.Dash(__name__, suppress_callback_exceptions = True, 
    title = 'Plotly Holiday Challenge Churn', 
    #update_title=None, 
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
    
)

# flask_app = app.server

# # Setup a flask 'app' as normal

# # Attach ScoutApm to the Flask App

# ScoutApm(flask_app)
# flask_app.config["SCOUT_NAME"] = "first app"

#new comment
