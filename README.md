# Plotly Holiday Challenge - Customer Churn Data

This project is for the 2022 Plotly Holiday Challenge. The goal was to create a dashboard that shows customer segmentation based on whether or not the customer has churned.

### Dashboard Walk Through

#### Home Page/Customer Base

- This page aims to show the demographics of the current customer base (where churn == "Yes").
- I added on customer location information to show services by location. The darker the color, the more customer in that location.
- I created this page to be a high level/executive view on many different metrics for the company.

#### Churn Investigation

- User interaction is required for this page to provide information.
- Select a column and see the churn breakdown by each value.
- The blue icons in the top right of each paper pop up a modal and show the top churn categories.
- Be sure to check out both the categorical and numeric breakdowns.

#### Churn Prediction

- I created a random forest classifier model to predict whether a customer would churn or not.
- The dropdowns on this page are fed into this model to predict the possibility of this individual churning or not.
- Our target class is actually 0, since we don't want our customers to churn.
- You can randomize a customer or create your own. The probability is in the progress bar below. Green is no churn, red is churn.
- The blue 'i' icon gives a high level summary of the models and my process.


### Notes and More

- Check out my jupyter notebook for my model, playground.ipynb
- I am using Dash Mantine Components as my main layout components.
- I am using Dash Design Kit for my graphs. I am not publicizing my Dash Enterprise url. You can replace ddk.Graph with dcc.Graph
- You can use requirements.txt to install the packages and run locally.

