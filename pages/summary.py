import dash
from dash import Input, Output, State, html, dcc, dash_table, MATCH, ALL, ctx
import dash_mantine_components as dmc
from dash_iconify import DashIconify
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, time, timedelta
import time as time_pck
import os
import dash_daq as daq
import pickle
import random

from app import app

def create_dropdown(id,label, options_list):
    return dmc.Select(
        id = id,
        label = label,
        data = [{'value':i, 'label': i} for i in options_list],
        value = options_list[0]
    )

df = pd.read_csv('data/customer-churn.csv')

custs = pd.read_csv('data/customer-churn.csv')


layout = html.Div(
    children=[
        dmc.Title(children = 'Churn Predicition', order = 3, style = {'font-family':'IntegralCF-ExtraBold', 'text-align':'center', 'color' :'slategray'}),
        dmc.Modal(
            id = 'info-ml',
            size = '75%',
            overflow="inside",
            title = [dmc.Title('Model Info', order = 3)],
            children = [
                dmc.Divider(label = 'AUC Curves and Model Performance', labelPosition = 'center'),
                dmc.SimpleGrid(
                    cols = 2,
                    children = [
                        dmc.Title('AUC - Original Data', order = 4, style = {'text-align':'center'}),
                        dmc.Title('AUC- Balanced Data', order = 4, style = {'text-align':'center'}),
                        html.Img(
                            src = app.get_asset_url('ml images/auc output.png'),
                            style = {'width':'25vw','justify-self':'center'}, 
                        ),
                        html.Img(
                            src = app.get_asset_url('ml images/auc balanced output.png'),
                            style = {'width':'25vw','justify-self':'center'}
                        ),
                        dmc.Text('We had a Yes-No ratio of approx. 4:1. This was the model generated with that data.', style= {'justify-self':'center'}),
                        dmc.Text('I balanced the Yes-No ratio to 1:1 with SMOTE. This is the new model. It performs better', style= {'justify-self':'center'}),
                    ]
                ),
                dmc.Divider(label = 'Confusion Matrix', labelPosition='center'),
                dmc.Stack(
                    align = 'center',
                    children = [
                        dmc.Title('Random Forest Confusion Matrix', order = 4, style = {'text-align':'center'}),
                        html.Img(
                            src = app.get_asset_url('ml images/confusion matrix rfc.png'),
                            style = {'width':'25vw','justify-self':'center'}, 
                        ),
                        dmc.Text('I choose the random forest classifier model from above. This is the confusion matrix for said model.', style = {'justify-self':'center'})
                    ]
                )
            ]
        ),
        dmc.Paper(
            m = 'sm',
            pb = 'sm',
            shadow = 'md',
            withBorder = True,
            radius = 'md',
            children = [
                dmc.Stack(
                    align = 'center',
                    children = [
                        # dmc.Title('Churn Scenario Probability', order= 3),
                        dmc.Divider(label = 'Based off Random Forest Classifier', labelPosition='center'),
                        dmc.Title('Create a customer below', order = 4, style = {'text-align':'center'}),
                        dmc.Button( id = 'randomize', children = 'Randomize a Customer', size = 'sm'),
                        dmc.SimpleGrid(
                            cols = 4,
                            children = [
                                # customerID,gender,SeniorCitizen,Partner,Dependents,tenure,PhoneService,MultipleLines,InternetService,OnlineSecurity,OnlineBackup,DeviceProtection,
                                # TechSupport,StreamingTV,StreamingMovies,Contract,PaperlessBilling,PaymentMethod,MonthlyCharges,TotalCharges,Churn


                                create_dropdown('select-gender', 'Gender', df.gender.unique()),
                                create_dropdown('senior-citizen', 'Senior Citizen', ['Yes', 'No']),
                                create_dropdown('select-partner', 'Partner', df.Partner.unique()),
                                create_dropdown('select-dependents', 'Dependents', df.Dependents.unique()),
                                dmc.NumberInput(id = 'input-tenure', label = 'Tenure (Months)', value = 12),
                                create_dropdown('phone-service', 'Phone Service', df.PhoneService.unique()),
                                create_dropdown('mult-line', 'Multiple Lines', df.MultipleLines.unique()),
                                create_dropdown('internet-service', 'Internet Service', df.InternetService.unique()),
                                create_dropdown('online-security', 'Online Security', df.OnlineSecurity.unique()),
                                create_dropdown('online-backup', 'Online Backup', df.OnlineBackup.unique()),
                                create_dropdown('device-protection', 'Device Protection', df.DeviceProtection.unique()),
                                create_dropdown('tech-support', 'Tech Support', df.TechSupport.unique()),
                                create_dropdown('streaming-tv', 'Streaming TV', df.StreamingTV.unique()),
                                create_dropdown('streaming-movies', 'Streaming Movies', df.StreamingMovies.unique()),
                                create_dropdown('select-contract', 'Contract', df.Contract.unique()),
                                create_dropdown('paperless-billing', 'Paperless Billing', df.PaperlessBilling.unique()),
                                create_dropdown('payment-method', 'Payment Method', df.PaymentMethod.unique()),
                                dmc.NumberInput(id = 'monthly-charges', label = 'Monthly Charges ($)', value = 50),
                                #create_dropdown('monthly-charges', 'Monthly Charges', df.MonthlyCharges.unique()),
                                dmc.NumberInput(id = 'total-charges', label = 'Total Charges ($ Tenure x Monthly Charges)', value = 0, disabled=True)
                                #dmc.NumberInput(id = 'input-monthly', label = 'Monthly Charges (', value = 12),
                                # dmc.Select(
                                #     id = 'select-gender',
                                #     style = {'width':'200px'},
                                #     label = 'Gender'
                                # ),
                                # dmc.Select(
                                #     id = 'senior-citizen',
                                #     label = 'Senior Citizen'
                                # ),
                            ]
                        ),
                        dmc.Button(id = 'submit-customer', children = 'Submit'),

                        dmc.Group(spacing = 'sm', children = [dmc.Title('Predicted Churn Probability', order = 3),dmc.ActionIcon(id = 'more-info', color = 'blue', size = 'lg', children = [DashIconify(icon = 'material-symbols:info', width = 24)])]),
                        dmc.Text(size = 'xs', color = 'dimmed', children = 'We want low % of churn!'),
                        dmc.Progress(id = 'probability', value=37.8, class_name = 'progressbar', color = 'green', label = '37.8%', size = 'xl'),
                        
                        #dmc.Text(id = 'probability', children = 'N/A Probability')
                        
                    ]
                )
            ]
        )
    ]
)


# customerID,gender,SeniorCitizen,Partner,Dependents,tenure,PhoneService,MultipleLines,InternetService,OnlineSecurity,OnlineBackup,DeviceProtection,
# TechSupport,StreamingTV,StreamingMovies,Contract,PaperlessBilling,PaymentMethod,MonthlyCharges,TotalCharges,Churn


@app.callback(Output('total-charges', 'value'),
                Input('input-tenure','value'),
                Input('monthly-charges', 'value'))
def update_test(tenure, mc):

    #print(tenure * mc)

    return tenure * mc


@app.callback(Output('probability', 'label'),
                Output('probability', 'value'),
                Output('probability', 'color'),
                Output('select-gender', 'value'),
                Output('senior-citizen', 'value'),
                Output('select-partner', 'value'),
                Output('select-dependents', 'value'),
                Output('input-tenure', 'value'),
                Output('phone-service', 'value'),
                Output('mult-line', 'value'),
                Output('internet-service', 'value'),
                Output('online-security','value'),
                Output('online-backup', 'value'),
                Output('device-protection', 'value'),
                Output('tech-support', 'value'),
                Output('streaming-tv', 'value'),
                Output('streaming-movies', 'value'),
                Output('select-contract','value'),
                Output('paperless-billing', 'value'),
                Output('payment-method', 'value'),
                Output('monthly-charges', 'value'),
                Input('submit-customer', 'n_clicks'),
                Input('randomize', 'n_clicks'),
                State('select-gender', 'value'),
                State('senior-citizen', 'value'),
                State('select-partner', 'value'),
                State('select-dependents', 'value'),
                State('input-tenure', 'value'),
                State('phone-service', 'value'),
                State('mult-line', 'value'),
                State('internet-service', 'value'),
                State('online-security','value'),
                State('online-backup', 'value'),
                State('device-protection', 'value'),
                State('tech-support', 'value'),
                State('streaming-tv', 'value'),
                State('streaming-movies', 'value'),
                State('select-contract','value'),
                State('paperless-billing', 'value'),
                State('payment-method', 'value'),
                State('monthly-charges', 'value'),
                #create_dropdown('monthly-charges', 'Monthly Charges', df.MonthlyCharges.unique()),
                State('total-charges', 'value'),
                prevent_inital_update = True,
                )
def update_prob(n , randomize, gender, citizen, partner, dependents, tenure, phoneservice, mutliline, interetsecurity, onlinesecurity, onlinebackup, devicprotection, techsupport, streamingtv, streamingmovies, contract, paperlessbilling, paymentmethod, monthlycharges, totalcharges):
    
    if ctx.triggered_id == 'submit-customer' or ctx.triggered_id is None:
        if citizen == 'Yes':
            citizen = 1
        else:
            citizen = 0

        #print(dependents)

        input_df = pd.DataFrame(
            data = [[1,gender, citizen, partner, dependents, tenure, phoneservice, mutliline, interetsecurity, onlinesecurity, onlinebackup, devicprotection, techsupport, streamingtv, streamingmovies, contract, paperlessbilling, paymentmethod, monthlycharges, totalcharges]], 
            columns = ['customerID','gender','SeniorCitizen','Partner','Dependents','tenure','PhoneService','MultipleLines','InternetService','OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport','StreamingTV','StreamingMovies','Contract','PaperlessBilling','PaymentMethod','MonthlyCharges','TotalCharges']
        )

        custs = pd.read_csv('data/customer-churn.csv')

        custs = pd.concat([custs, input_df], ignore_index=False)

        custs.drop(columns = ['Churn', 'customerID'], inplace = True)

        def yes_no(value, custs):
            custs[value] = custs[value].map({'Yes': 1, 'No': 0})
            return custs

        #custs = yes_no('Dependents', custs)
        custs = yes_no('Dependents',custs)
        custs = yes_no('Partner',custs)
        custs = yes_no('PhoneService', custs)
        #custs = yes_no('OnlineSecurity')
        #custs = yes_no('DeviceProtection')
        #custs = yes_no('TechSupport')
        #custs = yes_no('StreamingTV')
        #custs = yes_no('StreamingMovies')
        custs = yes_no('PaperlessBilling', custs)
        #yes_no('Churn')
        #yes_no('OnlineBackup')

        def dummy_creation(col, custs):
            dummy = pd.get_dummies(custs[col], prefix = str(col + '_'))

            custs = pd.concat([custs, dummy], axis = 1)

            custs.drop(columns = [col], inplace = True)

            #print(custs)

            return custs

        custs = dummy_creation('gender', custs)
        custs = dummy_creation('MultipleLines', custs)
        custs = dummy_creation('InternetService', custs)
        custs = dummy_creation('Contract', custs)
        custs = dummy_creation('PaymentMethod', custs)
        custs = dummy_creation('OnlineSecurity', custs)
        custs = dummy_creation('DeviceProtection', custs)
        custs = dummy_creation('TechSupport', custs)
        custs = dummy_creation('StreamingTV', custs)
        custs = dummy_creation('StreamingMovies', custs)
        custs = dummy_creation('OnlineBackup', custs)

        custs['TotalCharges'] = custs['TotalCharges'].replace(' ',0).astype(float)
        cols_to_norm = ['MonthlyCharges', 'TotalCharges', 'tenure']
        custs[cols_to_norm] = custs[cols_to_norm].apply(lambda x: (x - x.min()) / (x.max() - x.min()))

        with open('rf_model.pickle', 'rb') as f:
            rf = pickle.load(f)

        vals = rf.predict_proba(custs.tail(1))[0][1] * 100

        if vals > 50:
            color = 'red'
        elif vals < 50:
            color = 'green'
        else:
            color = 'yellow'

        probby = ('{:,.1f}%'.format(rf.predict_proba(custs.tail(1))[0][1] * 100))

        #print(custs)

        return probby, vals, color, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update
    elif ctx.triggered_id == 'randomize':
        vals = []
        columns = ['gender','SeniorCitizen','Partner','Dependents','tenure','PhoneService','MultipleLines','InternetService','OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport','StreamingTV','StreamingMovies','Contract','PaperlessBilling','PaymentMethod','MonthlyCharges','TotalCharges']

        for i in columns:
            choose_from = df[i].unique()

            length_of_choose = len(choose_from)
            rng_value = random.randint(0,length_of_choose - 1)

            vals.append(choose_from[rng_value])

        
        gender = vals[0]
        citizen = vals[1]
        partner = vals[2]
        dependents = vals[3]
        tenure = vals[4]
        phoneservice = vals [5]
        mutliline = vals[6]
        interetsecurity = vals[7]
        onlinesecurity = vals[8]
        onlinebackup = vals[9]
        devicprotection = vals[10]
        techsupport = vals[11]
        streamingtv = vals [12]
        streamingmovies = vals[13]
        contract = vals[14]
        paperlessbilling = vals[15]
        paymentmethod = vals[16]
        monthlycharges = vals [17]
        totalcharges = tenure * monthlycharges

        input_df = pd.DataFrame(
            data = [[1,gender, citizen, partner, dependents, tenure, phoneservice, mutliline, interetsecurity, onlinesecurity, onlinebackup, devicprotection, techsupport, streamingtv, streamingmovies, contract, paperlessbilling, paymentmethod, monthlycharges, totalcharges]], 
            columns = ['customerID','gender','SeniorCitizen','Partner','Dependents','tenure','PhoneService','MultipleLines','InternetService','OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport','StreamingTV','StreamingMovies','Contract','PaperlessBilling','PaymentMethod','MonthlyCharges','TotalCharges']
        )

        custs = pd.read_csv('data/customer-churn.csv')

        custs = pd.concat([custs, input_df], ignore_index=False)

        custs.drop(columns = ['Churn', 'customerID'], inplace = True)

        def yes_no(value, custs):
            custs[value] = custs[value].map({'Yes': 1, 'No': 0})
            return custs

        #custs = yes_no('Dependents', custs)
        custs = yes_no('Dependents',custs)
        custs = yes_no('Partner',custs)
        custs = yes_no('PhoneService', custs)
        #custs = yes_no('OnlineSecurity')
        #custs = yes_no('DeviceProtection')
        #custs = yes_no('TechSupport')
        #custs = yes_no('StreamingTV')
        #custs = yes_no('StreamingMovies')
        custs = yes_no('PaperlessBilling', custs)
        #yes_no('Churn')
        #yes_no('OnlineBackup')

        def dummy_creation(col, custs):
            dummy = pd.get_dummies(custs[col], prefix = str(col + '_'))

            custs = pd.concat([custs, dummy], axis = 1)

            custs.drop(columns = [col], inplace = True)

            #print(custs)

            return custs

        custs = dummy_creation('gender', custs)
        custs = dummy_creation('MultipleLines', custs)
        custs = dummy_creation('InternetService', custs)
        custs = dummy_creation('Contract', custs)
        custs = dummy_creation('PaymentMethod', custs)
        custs = dummy_creation('OnlineSecurity', custs)
        custs = dummy_creation('DeviceProtection', custs)
        custs = dummy_creation('TechSupport', custs)
        custs = dummy_creation('StreamingTV', custs)
        custs = dummy_creation('StreamingMovies', custs)
        custs = dummy_creation('OnlineBackup', custs)

        custs['TotalCharges'] = custs['TotalCharges'].replace(' ',0).astype(float)
        cols_to_norm = ['MonthlyCharges', 'TotalCharges', 'tenure']
        custs[cols_to_norm] = custs[cols_to_norm].apply(lambda x: (x - x.min()) / (x.max() - x.min()))

        with open('rf_model.pickle', 'rb') as f:
            rf = pickle.load(f)

        vals = rf.predict_proba(custs.tail(1))[0][1] * 100

        if vals > 50:
            color = 'red'
        elif vals < 50:
            color = 'green'
        else:
            color = 'yellow'

        probby = ('{:,.1f}%'.format(rf.predict_proba(custs.tail(1))[0][1] * 100))

        #print(custs)

        if citizen == 0:
            citizen = 'No'
        else:
            citizen = 'Yes'
        

        return probby, vals, color, gender, citizen, partner, dependents, tenure, phoneservice, mutliline, interetsecurity, onlinesecurity, onlinebackup, devicprotection, techsupport, streamingtv, streamingmovies, contract, paperlessbilling, paymentmethod, monthlycharges


@app.callback(Output('info-ml', 'opened'),
                Input('more-info', 'n_clicks'),
                State('info-ml', 'opened'))
def open_modal(n, opened):
    if ctx.triggered_id is not None:
        return not opened
    else:
        return False