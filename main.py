from flask import Flask, request
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import numpy as np

app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return """
    <h1>Welcome to Employee Absenteeism Prediction</h1>
    <p>click start to continue<br>
    <button onclick="location.href = '/html';" id="myButton" >start</button>
    """

@app.route('/prediction')
def prediction():
    variables = request.args.to_dict(flat=True)
    value_list=list(variables.values())
    input = [value_list]
    # Reason = request.args.get('Reason')
    # Season = request.args.get('Seasons')
    # Distance = request.args.get('Distance')
    # Age = request.args.get('Age')
    # Workload = request.args.get('Workload')
    # Hittarget = request.args.get('Hittarget')
    # Disciplinary = request.args.get('Disciplinary')
    # Education = request.args.get('Education')
    # Son = request.args.get('Son')
    # Drinker = request.args.get('Drinker')
    # Smoker = request.args.get('Smoker')
    # Pet = request.args.get('Pet')
    # BMI = request.args.get('BMI')



    data = pd.read_csv("data/Absenteeism_at_work.csv", sep = ';')
    data.drop(['ID'], axis = 1, inplace = True)
    data['absence'] = data['Absenteeism time in hours'] > 1
    data.drop(['Absenteeism time in hours', 'Month of absence', 'Day of the week', 'Weight', 'Height', 'Transportation expense', 'Service time'], axis = 1, inplace = True)

    X = data.drop(['absence'], axis = 1)
    y = data['absence']

    X["Reason for absence"] = X["Reason for absence"].astype("category")
    X["Seasons"] = X["Seasons"].astype("category")
    X["Disciplinary failure"] = X["Disciplinary failure"].astype("category")
    X["Education"] = X["Education"].astype("category")
    X["Social drinker"] = X["Social drinker"].astype("category")
    X["Social smoker"] = X["Social smoker"].astype("category")


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    

    clf = RandomForestClassifier(#min_impurity_decrease = 1e-6,
                                #n_estimators = 200, 
                                class_weight = 'balanced_subsample', random_state=42).fit(X_train, y_train)
    clf.score(X_test, y_test)
    res = clf.predict(input) 
    
    if res[0]:
        return '''
            <h1>The employee is likely to be absent</h1>
            <button onclick="location.href = '/';" id="myButton" >Home</button>
            <button onclick="location.href = '/html';" id="myButton" >Try agian</button>
        '''
    else:
        return '''
            <h1>The employee is not likely to be absent</h1>
            <button onclick="location.href = '/';" id="myButton" >Home</button>
            <button onclick="location.href = '/html';" id="myButton" >Try agian</button>
        '''

@app.route('/html')
def html():
    """Returns some custom HTML"""
    return """
    <div style="position: absolute; right: 800px;">
    <h2>Code Book</h2><br>
        <img src="https://github.com/shangwenyan/IDS721FinalProject/blob/main/images/Codebook.png?raw=true" ></img>
    </div>
    <form action="/prediction", method="GET">
        <h1>Enter Employee Information</h1><br>        
        <label for="Reason">Reason for absence:</label><br>
        <input type="text" id="Reason" name="Reason" value=0><br>

        <label for="Seasons">Seasons:</label><br>
        <input type="text" id="Seasons" name="Seasons" value=0><br>

        <label for="Distance">Distance from Residence to Work:</label><br>
        <input type="text" id="Distance" name="Distance" value=0><br>

        <label for="Age">Age:</label><br>
        <input type="text" id="Age" name="Age" value=0><br>

        <label for="Workload">Work load Average/day:</label><br>
        <input type="text" id="Workload" name="Workload" value=0><br>

        <label for="Hittarget">Hit target:</label><br>
        <input type="text" id="Hittarget" name="Hittarget" value=0><br>

        <label for="Disciplinary">Disciplinary failure:</label><br>
        <input type="text" id="Disciplinary" name="Disciplinary" value=0><br>

        <label for="Education">Education:</label><br>
        <input type="text" id="Education" name="Education" value=0><br>

        <label for="Son">Son:</label><br>
        <input type="text" id="Son" name="Son" value=0><br>

        <label for="Drinker">Drinker:</label><br>
        <input type="text" id="Drinker" name="Drinker" value=0><br>

        <label for="Smoker">Smoker:</label><br>
        <input type="text" id="Smoker" name="Smoker" value=0><br>

        <label for="Pet">Pet:</label><br>
        <input type="text" id="Pet" name="Pet" value=0><br>

        <label for="BMI">BMI:</label><br>
        <input type="text" id="BMI" name="BMI" value=0><br>
        
        <input type="submit" value="Predict">
    </form> 
    <button onclick="location.href = '/';" id="myButton" >Home</button><br>


    """



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)