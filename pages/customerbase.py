import dash
import dash_design_kit as ddk
from dash import Input, Output, State, html, dcc, dash_table, MATCH, ALL, ctx
import dash_mantine_components as dmc
from dash_iconify import DashIconify
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, time, timedelta
import time as time_pck
import os
import dash_daq as daq
import plotly.express as px
import plotly.graph_objects as go

from app import app

layout = html.Div(
    style= {'margin-top':'70px'},
    children=[
        dmc.Group(
            direction = 'column',
            grow = True,
            children = [
                dmc.Title(children = 'Customer Base', order = 3, style = {'font-family':'IntegralCF-ExtraBold', 'text-align':'center', 'color' :'slategray'}),
                #dmc.Space(),
                #dmc.Space(),
                dmc.Divider(label = 'Overview',  labelPosition='center', size='xl'),
                dmc.Group(
                    direction = 'row',
                    grow = True,
                    children = [
                        dmc.Paper(
                            radius="md", # or p=10 for border-radius of 10px
                            withBorder=True,
                            shadow='xs',
                            p='sm',
                            style={'height':'175px'},
                            children=[
                                dmc.Center(
                                    dmc.ThemeIcon(
                                        size=50,
                                        radius="xl",
                                        color="violet",
                                        variant="light",
                                        children=[DashIconify(icon="fluent:people-community-20-filled", width=30)]
                                    )
                                ),
                                dmc.Group(
                                    direction='column',
                                    position='center',
                                    spacing='xs',
                                    style={'margin-top':10},
                                    children=[
                                        dmc.Text('Current Number of Customers', size='xs', color='dimmed', style={'font-family':'IntegralCF-RegularOblique'}),
                                        dmc.Text(id='totalcust', size='xl', style={'font-family':'IntegralCF-ExtraBold'}),
                                        dmc.Text('Churn Rate', id = 'churn_rate', size='xs', color='red', style={'font-family':'IntegralCF-RegularOblique'})
                                    ]
                                )
                            ],
                        ),
                        dmc.Paper(
                            radius="md", # or p=10 for border-radius of 10px
                            withBorder=True,
                            shadow='xs',
                            p='sm',
                            style={'height':'175px'},
                            children=[
                                dmc.Center(
                                    dmc.ThemeIcon(
                                        size=50,
                                        radius="xl",
                                        color="yellow",
                                        variant="light",
                                        children=[DashIconify(icon="mdi:recurring-payment", width=30)]
                                    )
                                ),
                                dmc.Group(
                                    direction='column',
                                    position='center',
                                    spacing='xs',
                                    style={'margin-top':10},
                                    children=[
                                        dmc.Text('Monthly Revenue', size='xs', color='dimmed', style={'font-family':'IntegralCF-RegularOblique'}),
                                        dmc.Text(id='revenue', size='xl', style={'font-family':'IntegralCF-ExtraBold'}),
                                        dmc.Text('*from current customers only', id = 'totalrev', size='xs', color='green', style={'font-family':'IntegralCF-RegularOblique'})
                                    ]
                                )
                            ],
                        ),
                        dmc.Paper(
                            radius="md", # or p=10 for border-radius of 10px
                            withBorder=True,
                            shadow='xs',
                            p='sm',
                            style={'height':'175px'},
                            children=[
                                dmc.Center(
                                    dmc.ThemeIcon(
                                        size=50,
                                        radius="xl",
                                        color="green",
                                        variant="light",
                                        children=[DashIconify(icon="mdi:ecology", width=30)]
                                    )
                                ),
                                dmc.Group(
                                    direction='column',
                                    position='center',
                                    spacing='xs',
                                    style={'margin-top':10},
                                    children=[
                                        dmc.Text('Paperless Billing Accounts', size='xs', color='dimmed', style={'font-family':'IntegralCF-RegularOblique'}),
                                        dmc.Text(id='paperless', size='xl', style={'font-family':'IntegralCF-ExtraBold'}),
                                        dmc.Text('Reams Saved', id = 'reams_saved', size='xs', color='green', style={'font-family':'IntegralCF-RegularOblique'})
                                    ]
                                )
                            ],
                        ),
                    ]
                ),
                dmc.Divider(label = 'Demographics', labelPosition='center', size='xl'),
                dmc.Group(
                    direction = 'row',
                    grow = True,
                    children = [
                        dmc.Paper(
                            radius="md", # or p=10 for border-radius of 10px
                            withBorder=True,
                            shadow='xs',
                            p='sm',
                            style={'height':'350px'},
                            children=[
                                dmc.Title('Gender', order = 4, style = {'font-family':'IntegralCF-Regular','text-align':'center', 'color':'grey', 'letter-spacing':'1px'}),
                                ddk.Graph(id='gender'),
                            ]
                        ),
                        dmc.Paper(
                            radius="md", # or p=10 for border-radius of 10px
                            withBorder=True,
                            shadow='xs',
                            p='sm',
                            style={'height':'350px'},
                            children=[
                                dmc.Title('Household', order = 4, style = {'font-family':'IntegralCF-Regular','text-align':'center', 'color':'grey', 'letter-spacing':'1px'}),
                                ddk.Graph(id='household')
                            ]
                        ),
                        dmc.Paper(
                            radius="md", # or p=10 for border-radius of 10px
                            withBorder=True,
                            shadow='xs',
                            p='sm',
                            style={'height':'350px'},
                            children=[
                                dmc.Title('Senior Citizen Status', order = 4, style = {'font-family':'IntegralCF-Regular','text-align':'center', 'color':'grey', 'letter-spacing':'1px'}),
                                ddk.Graph(id = 'age')
                            ]
                        ),
                    ]
                ),
                dmc.Group(
                    direction = 'row',
                    grow = True,
                    children = [
                        dmc.Paper(
                            radius="md", # or p=10 for border-radius of 10px
                            withBorder=True,
                            shadow='xs',
                            p='sm',
                            style={'height':'500px'},
                            children=[
                                dmc.Title('Customer Density', order = 4, style = {'font-family':'IntegralCF-Regular','text-align':'center', 'color':'grey', 'letter-spacing':'1px'}),
                                ddk.Graph(id = 'locations_map')
                            ]
                        ),
                        dmc.Paper(
                            radius="md", # or p=10 for border-radius of 10px
                            withBorder=True,
                            shadow='xs',
                            p='sm',
                            style={'height':'500px'},
                            children=[
                                dmc.Title('Customers W/O Phone Service', order = 4, style = {'font-family':'IntegralCF-Regular','text-align':'center', 'color':'grey', 'letter-spacing':'1px'}),
                                ddk.Graph(id = 'locations_map1')
                            ]
                        ),
                        dmc.Paper(
                            radius="md", # or p=10 for border-radius of 10px
                            withBorder=True,
                            shadow='xs',
                            p='sm',
                            style={'height':'500px'},
                            children=[
                                dmc.Title('Customers W/O Internet Service', order = 4, style = {'font-family':'IntegralCF-Regular','text-align':'center', 'color':'grey', 'letter-spacing':'1px'}),
                                ddk.Graph(id = 'locations_map2')
                            ]
                        ),
                    ]
                ),
            
                
                
                dmc.Space(h=50)
            ]
        )
    ]
)


@app.callback(Output('totalcust', 'children'),
                Output('churn_rate','children'),
                Output('paperless', 'children'),
                Output('reams_saved', 'children'),
                Output('revenue', 'children'),
                Output('totalrev', 'children'),
                Input('url','pathname')
)
def update_card1(n):

    df = pd.read_csv('data/customer-churn.csv')

    sc = df.query('Churn == "No"')
    sc['TotalCharges'] = sc.TotalCharges.replace(' ', 0).astype(float)

    sc = sc.infer_objects()
    sc['tenureYears'] = sc.tenure/12

    te = df['Churn'].replace('Yes',1).replace('No',0).astype(int).mean()

    ps = sc.query('PaperlessBilling == "Yes"').shape[0]

    reams_saved = int(round((ps * 12 * 3)/500))

    sc['TotalCharges'] = sc.TotalCharges.replace(' ', 0).astype(float)

    rev = sc.MonthlyCharges.sum()

    atr = sc.TotalCharges.sum()

    return "{:,}".format(sc.customerID.nunique()), f'{"{:.2f}%".format(te * 100)} Churn Rate', "{:,}".format(ps), f'Approx. {reams_saved} Reams Saved Per Year', "${:,.2f}".format(rev), f'{"${:,.2f}".format(atr)} *all time'




@app.callback(Output('gender' ,'figure'),
                Output('household','figure'),
                Output('age', 'figure'),
                Input('url', 'pathname'),
)
def update_graphs(n):

    df = pd.read_csv('data/customer-churn.csv')

    sc = df.query('Churn == "No"')

    fig = px.pie(
        sc,
        names='gender',
        color = 'gender',
        hole=0.5,
        labels = ['Female' ,'Male'],
        color_discrete_map={'Male':'#0F203A',
                            'Female':'#F39A59',
        }
        
    )
    fig.update_traces(textposition='outside', textinfo='percent+label+value', hovertemplate = "%{customdata[0]}<extra></extra>",)
    fig.update_layout(showlegend = False, plot_bgcolor = '#fff', paper_bgcolor = '#fff', height = 300)


    hh = sc[['Partner','Dependents']].groupby(['Partner','Dependents']).size().to_frame().reset_index()

    fig1 = px.bar(
        hh,
        x = 'Partner',
        y = 0,
        color = 'Dependents',
        barmode = 'group',
        text_auto=True,
        color_discrete_map={'No':'#cbccce',
                            'Yes':'#174b7d',
        }
    )
    fig1.update_yaxes(range = [0,hh[0].max()*1.2], title = '# of Customers')
    fig1.update_traces(texttemplate="%{y:,}")
    fig1.update_layout(plot_bgcolor = '#fff', paper_bgcolor = '#fff', height = 300)

    sc['SeniorCitizen'] = sc['SeniorCitizen'].replace(1,'Yes').replace(0,'No')

    old = sc[['SeniorCitizen']].groupby('SeniorCitizen').size().to_frame().reset_index()
    
    fig2 = px.bar(
        old,
        x="SeniorCitizen",
        y=0, 
        color="SeniorCitizen",
        color_discrete_map={'No':'#cbccce',
                            'Yes':'#174b7d',
        }
    )
    fig2.update_yaxes(range = [0,old[0].max()*1.2], title = '# of Customers')
    fig2.update_traces(texttemplate="%{y:,}")
    fig2.update_layout(showlegend = False, plot_bgcolor = '#fff', paper_bgcolor = '#fff', height = 300)

    return fig, fig1, fig2


@app.callback(Output('locations_map','figure'),
                Input('url','pathname'))
def update_locations(n):

    df = pd.read_csv('data/full_cust_info.csv')

    df = df.query('Churn == "No"').reset_index(drop = True)

    fig = go.Figure()

    mapbox_access_token = 'pk.eyJ1Ijoia3JpdGhpY2hhbmRyYWthc2FuIiwiYSI6ImNrbWYwemVmNzEwZDMyd2xqNHJ6MTc5MGgifQ.QSmii-0BmMoAPYkQDMBvkw'

    fig.add_trace(
        go.Scattermapbox(
            lat=df['Latitude'].tolist(),
            lon=df['Longitude'].tolist(),
            #text=df['Display Name'].tolist(),
            #customdata=nk,
            mode='markers',
            marker=go.scattermapbox.Marker(
                size=7,
                color='rgba(245,98,57,0.1)',
                #opacity = .3
            ),
            #hoverinfo='none',
            #hovertemplate="<br>".join([
            #    "<br><b>%{text}</b><br>",
            #    "%{customdata[0]}",
            #    "%{customdata[1]},"+
            #    " %{customdata[2]}"+
            #    " %{customdata[3]}<extra></extra>",
            #])
        )
    )

    fig.update_layout(
        autosize=True,
        hovermode='closest',
        mapbox=dict(
            style='light',
            accesstoken=mapbox_access_token,
            bearing=0,
            center=dict(
                lat=37.339039629245576,
                lon=-119.49106041519023,
            ),
            pitch=5, #30
            zoom=4.55
        ),
    )

    return fig

@app.callback(Output('locations_map1','figure'),
                Input('url','pathname'))
def update_locations(n):

    df = pd.read_csv('data/full_cust_info.csv')

    df = df.query('Churn == "No"').reset_index(drop = True)

    df = df.query('PhoneService == "No"')

    fig = go.Figure()


    mapbox_access_token = 'pk.eyJ1Ijoia3JpdGhpY2hhbmRyYWthc2FuIiwiYSI6ImNrbWYwemVmNzEwZDMyd2xqNHJ6MTc5MGgifQ.QSmii-0BmMoAPYkQDMBvkw'

    fig.add_trace(
        go.Scattermapbox(
            lat=df['Latitude'].tolist(),
            lon=df['Longitude'].tolist(),
            #text=df['Display Name'].tolist(),
            #customdata=nk,
            mode='markers',
            marker=go.scattermapbox.Marker(
                size=7,
                color='rgba(245,98,57,0.1)',
                
                #opacity = 0.1
            ),
            #hoverinfo='none',
            #hovertemplate="<br>".join([
            #    "<br><b>%{text}</b><br>",
            #    "%{customdata[0]}",
            #    "%{customdata[1]},"+
            #    " %{customdata[2]}"+
            #    " %{customdata[3]}<extra></extra>",
            #])
        )
    )

    fig.update_layout(
        autosize=True,
        hovermode='closest',
        mapbox=dict(
            style='light',
            accesstoken=mapbox_access_token,
            bearing=0,
            center=dict(
                lat=37.339039629245576,
                lon=-119.49106041519023,
            ),
            pitch=5, #30
            zoom=4.55
        ),
    )
    return fig


@app.callback(Output('locations_map2','figure'),
                Input('url','pathname'))
def update_locations(n):

    df = pd.read_csv('data/full_cust_info.csv')

    df = df.query('Churn == "No"').reset_index(drop = True)
    df = df.query('InternetService == "No"')

    fig = go.Figure()


    mapbox_access_token = 'pk.eyJ1Ijoia3JpdGhpY2hhbmRyYWthc2FuIiwiYSI6ImNrbWYwemVmNzEwZDMyd2xqNHJ6MTc5MGgifQ.QSmii-0BmMoAPYkQDMBvkw'

    fig.add_trace(
        go.Scattermapbox(
            lat=df['Latitude'].tolist(),
            lon=df['Longitude'].tolist(),
            #text=df['Display Name'].tolist(),
            #customdata=nk,
            mode='markers',
            marker=go.scattermapbox.Marker(
                size=7,
                color='rgba(245,98,57,0.1)',
                #opacity = 0.1
            ),
            #hoverinfo='none',
            #hovertemplate="<br>".join([
            #    "<br><b>%{text}</b><br>",
            #    "%{customdata[0]}",
            #    "%{customdata[1]},"+
            #    " %{customdata[2]}"+
            #    " %{customdata[3]}<extra></extra>",
            #])
        )
    )

    fig.update_layout(
        autosize=True,
        hovermode='closest',
        mapbox=dict(
            style='light',
            accesstoken=mapbox_access_token,
            bearing=0,
            center=dict(
                lat=37.339039629245576,
                lon=-119.49106041519023,
            ),
            pitch=5, #30
            zoom=4.55
        ),
    )

    return fig
