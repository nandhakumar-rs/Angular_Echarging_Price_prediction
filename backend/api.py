from flask import Flask,jsonify,request,json
from sklearn.preprocessing import Imputer
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
import numpy as np
import pandas as pd
from flask_cors import CORS


dataset = pd.read_csv("data.csv")
X  = dataset.iloc[:,1:-1]
Y =  dataset.iloc[:,11]
X["Accumulated GHG (kg)"] = X["Accumulated GHG (kg)"].apply(lambda x: float(x.split()[0].replace(',', '')))
# Y = Y.apply(lambda x: float(x.split("'")[0].replace(',', '')))
eliminate_zero = Y.mean()
Y = Y.mask(Y == 0, eliminate_zero)
X = X.values
Y = Y.values
imputer = Imputer(missing_values='NaN',strategy='mean',axis=0)
imputer = imputer.fit(X)
X= imputer.transform(X)
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=0)

app = Flask(__name__)
CORS(app)


@app.route('/linear-regression-prdiction',methods=['POST','GET'])
def linearRegressionPrediction():
    if request.method == 'POST':
        data = request.get_json()
        result = linearRegression(data['data'])
        print(result)
        return jsonify({"result":result})
    else:
        return jsonify({"result":"test"})

@app.route('/decision-tree-prdiction',methods=['POST','GET'])
def decisionTreePrediction():
    if request.method == 'POST':
        data = request.get_json()
        result = decisionTree(data['data'])
        print(result)
        return jsonify({"result":result})
    else:
        return jsonify({"result":"test"})

def linearRegression(value):
    linear_regression = LinearRegression()
    linear_regression.fit(X_train,Y_train)
    result = linear_regression.predict([value])
    print(result)
    return json.dumps({"data":result[0]})
    
def decisionTree(value):
    decision_tree_regression = DecisionTreeRegressor(random_state=0)
    decision_tree_regression.fit(X,Y)
    result = decision_tree_regression.predict([value])
    return json.dumps({"data":result[0]})

if __name__ == '__main__':
    app.run(debug=True)        