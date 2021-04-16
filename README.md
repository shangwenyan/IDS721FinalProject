# Predict Absenteeism at Work

## Data 

This dataset can be retrieved from [UCI Machine Learing Repository](https://archive.ics.uci.edu/ml/datasets/Absenteeism+at+work).

The original website is at [link](http://www.uninove.br/curso/informatica-e-gestao-do-conhecimento/).

The dataset contains 740 observations and 21 features on the profiles of employees who report their absenteeism.

Features include Reasons for absence,Seasons, Transportation Expense, etc.

## Model

Logistic regression, randomForest, and Gradient boosting are selected to model such phenomena.

As a result, RandomForest is the best to model absenteeism at work and the overall auc is 0.87.

## Integrated with Flask on GCP

The prediction panel is hosted on GCP flask and user can input their profile and get a prediction of whether they will be absent from work.

## Prediction Panel Demo

link:

Here is a demo about how the system works:
