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

df = pd.read_csv('data/customer-churn.csv')

layout = html.Div(
    style = {'overflow-x':'hidden'},
    children=[
        dmc.Modal(
            id = 'cat-table',
            size = 'xl',
            title = [dmc.Title('Top Churn Situations (Categorical)', order = 2)],
            children = [

            ]
        ),
        dmc.Modal(
            id = 'num-table',
            title = [dmc.Title('Top Churn Situations (Numerical)', order = 2)],
            children = [
                
            ]
        ),
        dmc.Group(
            direction = 'column',
            grow = True,
            position = 'center',
            spacing = 'sm',
            children = [
                dmc.Title(children = 'Churn Investigation', order = 3, style = {'font-family':'IntegralCF-ExtraBold','text-align':'center', 'color' :'slategray'}),
                # dmc.Divider(label = 'Churn vs Customer', labelPosition = 'center'),
                dmc.Paper(
                    shadow = 'md',
                    m = 'sm',
                    p = 'md',
                    #style = {'width':'90%'},
                    withBorder = True,
                    children = [
                        dmc.Stack(
                            children = [
                                dmc.Group(
                                    position = 'apart',
                                    children = [
                                        dmc.Title('Total Customers vs Categorical Metric', order = 4),
                                        dmc.ActionIcon(id = 'categorical-table', children = [DashIconify(icon = 'material-symbols:backup-table', width=24)], color = 'blue', variant = 'filled', size = 'lg')
                                    ]
                                ),
                                dmc.Stack(
                                    children = [
                                        dmc.Select(
                                            id = 'column_name',
                                            label = 'Select Column To Investigate (Categorical)',
                                            style= {'width':'50%','margin':'auto'},
                                            data = [
                                                {'label':i, 'value':i} for i in df.drop(columns = ['Churn','customerID', 'MonthlyCharges', 'TotalCharges' ,'tenure']).columns
                                            ],
                                            value = 'gender'
                                        ),
                                        dmc.Group(
                                            direction = 'row',
                                            position = 'center',
                                            children = [
                                                dmc.Badge('Churned', color = 'red', variant = 'filled'),
                                                dmc.Badge('Still A Customer', color = 'green', variant = 'filled')
                                            ]
                                        ),                                        
                                    ]
                                ),
                                ddk.Graph(id = 'compare_graph'),                                
                            ]
                        )
                    ]
                ),
                #ddk.Graph(id = 'compare_graph'),

                #dmc.Divider(label = 'Numerical Grouping', labelPosition = 'center'),
                dmc.Paper(
                    shadow = 'md',
                    m = 'sm',
                    p = 'md',
                    #style = {'width':'90%'},
                    withBorder = True,
                    children = [
                        dmc.Stack(
                            children = [
                                dmc.Group(
                                    position = 'apart',
                                    children = [
                                        dmc.Title('Total Customers vs Numerical Metric', order = 4),
                                        dmc.ActionIcon(id = 'table-nums', children = [DashIconify(icon = 'material-symbols:backup-table', width=24)], color = 'blue', variant = 'filled', size = 'lg')
                                    ]
                                ),
                                dmc.Select(
                                    id = 'column_name_num',
                                    label = 'Select Column To Investigate (Numerical)',
                                    style= {'width':'50%','margin':'auto'},
                                    data = [
                                        {'label':i, 'value':i} for i in df[['MonthlyCharges', 'TotalCharges', 'tenure']].columns
                                    ],
                                    value = 'tenure'
                                ),
                                dmc.Group(
                                    direction = 'row',
                                    position = 'center',
                                    children = [
                                        dmc.Badge('Churned', color = 'red', variant = 'filled'),
                                        dmc.Badge('Still A Customer', color = 'green', variant = 'filled')
                                    ]
                                ),
                                ddk.Graph(id = 'compare_graph_num'),
                            ]
                        ),
                    ]
                ),
            ]
        )
        
    ]
)


@app.callback(Output('compare_graph', 'figure'),
                Input('column_name','value'))
def update_graph(value):

    df = pd.read_csv('data/customer-churn.csv')

    df = df[['Churn',value]].groupby(['Churn', value]).size().to_frame().reset_index()

    df.columns = ['churn', 'value', 'count']

    fig = px.bar(df, x='value', y= 'count', color="churn", text='churn', color_discrete_map={
        'Yes':'rgb(250, 82, 82)',
        'No':'rgb(64, 192, 87)'
    })

    fig.update_traces(textposition='inside', texttemplate = "%{y:,} Customers", textfont = dict(color='white'))

    fig.update_xaxes(title = value)
    fig.update_yaxes(title = 'Total Customers')
    #fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')

    fig.update_layout(barmode='relative')

    fig.update_layout(showlegend = False, plot_bgcolor = '#fff', paper_bgcolor = '#fff')

    return fig

@app.callback(Output('compare_graph_num', 'figure'),
                Input('column_name_num','value'))
def update_graph(value):

    df = pd.read_csv('data/customer-churn.csv')

    if value == 'tenure':
        bins = [0,12,48,84]
        labels = ['New Customers', '1-4 Years', '4-7 Years']
        df['tenure'] = pd.cut(df['tenure'], bins=bins, labels=labels)
    elif value == 'MonthlyCharges':
        bins = [0,25,50,75,100, 100000]
        labels = ['$0 - $25', '$25 - $50', '$50 - $75' , '$75 - $100', '$100+']
        df['MonthlyCharges'] = pd.cut(df['MonthlyCharges'], bins=bins, labels=labels)
    elif value == 'TotalCharges':
        df['TotalCharges'] = df['TotalCharges'].replace(' ',0).astype(float)
        bins = [0, 1000, 4000, 8000, 15000]
        labels = ['Less than $1,000', '$1,000 - $4,000', '$4,000 - $8,000' , '$8,000+']
        df['TotalCharges'] = pd.cut(df['TotalCharges'], bins=bins, labels=labels)

    df = df[['Churn',value]].groupby(['Churn', value]).size().to_frame().reset_index()

    df.columns = ['churn', 'value', 'count']

    fig = px.bar(df, x='value', y= 'count', color="churn", text='churn', color_discrete_map={
        'Yes':'rgb(250, 82, 82)',
        'No':'rgb(64, 192, 87)'
    })

    fig.update_traces(textposition='inside', texttemplate = "%{y:,} Customers", textfont = dict(color='white'))

    fig.update_xaxes(title = value)
    fig.update_yaxes(title = 'Total Customers')
    #fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')

    fig.update_layout(barmode='relative')

    fig.update_layout(showlegend = False, plot_bgcolor = '#fff', paper_bgcolor = '#fff')

    return fig


@app.callback(Output('cat-table', 'children'),
                Output('cat-table', 'opened'),
                Input('categorical-table', 'n_clicks'),
                State('cat-table', 'opened'),
                prevent_inital_call = True)
def update_modal_cat(n, opened):

    if ctx.triggered_id is None:
        return [], False


    df = pd.read_csv('data/customer-churn.csv')

    df.drop(columns = ['tenure', 'TotalCharges', 'MonthlyCharges', 'customerID'], inplace = True)

    final_df = pd.DataFrame()

    for i in df.columns.tolist():
        if i == 'Churn':
            pass
        else:
            df1 = df[['Churn',i]].groupby(['Churn', i]).size().to_frame().reset_index()
            df1.columns = ['churn', 'value', 'count']

            df2 = df1.query('count > 1000 and churn == "Yes"')

            df2['metric'] = i

            final_df = pd.concat([final_df, df2[['metric', 'value', 'count', 'churn']]], ignore_index = True)


    print(final_df)

    return dash_table.DataTable(
        data = final_df.to_dict('records'),
        columns = [{'name':i, 'id':j} for i,j in zip(['Metric', 'Value', 'Count', 'Churn'], final_df.columns.tolist())],
        style_as_list_view=True,
    ), not opened

@app.callback(Output('num-table', 'children'),
                Output('num-table', 'opened'),
                Input('table-nums', 'n_clicks'),
                State('table-nums', 'opened'),
                prevent_inital_call = True)
def update_modal_cat(n, opened):

    if ctx.triggered_id is None:
        return [], False


    df = pd.read_csv('data/customer-churn.csv')

    df = df[['tenure', 'TotalCharges', 'MonthlyCharges', 'Churn']]

    final_df = pd.DataFrame()

    for i in df.columns.tolist():
        if i == 'Churn':
            pass
        else:

            if i == 'tenure':
                bins = [0,12,48,84]
                labels = ['New Customers', '1-4 Years', '4-7 Years']
                df['tenure'] = pd.cut(df['tenure'], bins=bins, labels=labels)
            elif i == 'MonthlyCharges':
                bins = [0,25,50,75,100, 100000]
                labels = ['$0 - $25', '$25 - $50', '$50 - $75' , '$75 - $100', '$100+']
                df['MonthlyCharges'] = pd.cut(df['MonthlyCharges'], bins=bins, labels=labels)
            elif i == 'TotalCharges':
                df['TotalCharges'] = df['TotalCharges'].replace(' ',0).astype(float)
                bins = [0, 1000, 4000, 8000, 15000]
                labels = ['Less than $1,000', '$1,000 - $4,000', '$4,000 - $8,000' , '$8,000+']
                df['TotalCharges'] = pd.cut(df['TotalCharges'], bins=bins, labels=labels)

            df1 = df[['Churn',i]].groupby(['Churn', i]).size().to_frame().reset_index()
            df1.columns = ['churn', 'value', 'count']

            df2 = df1.query('count > 1000 and churn == "Yes"')

            df2['metric'] = i

            final_df = pd.concat([final_df, df2[['metric', 'value', 'count', 'churn']]], ignore_index = True)


    print(final_df)

    return dash_table.DataTable(
        data = final_df.to_dict('records'),
        columns = [{'name':i, 'id':j} for i,j in zip(['Metric', 'Value', 'Count', 'Churn'], final_df.columns.tolist())],
        style_as_list_view=True,
    ), not opened




    #df = df[['Churn',value]].groupby(['Churn', value]).size().to_frame().reset_index()
