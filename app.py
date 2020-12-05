import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')





# def ValuePredictor(to_predict_list):
#     to_predict = np.array(to_predict_list).reshape(1,4)
#     loaded_model = pickle.load(open("model.pkl","rb"))
#     result = loaded_model.predict(to_predict)
#     return result[0]

@app.route('/predict',methods = ['POST'])

def predict():
    model=pickle.load(open('lr1.pkl','rb'))
    le=pickle.load(open('le1.pkl','rb'))
    rb=pickle.load(open('rb.pkl','rb'))
    location=request.form['location']
    sqft=request.form['sqft']
    bath=request.form['bath']
    bhk=request.form['bhk']
    list1=[[location,sqft,bath,bhk]]
    list2=pd.DataFrame(list1)
    list2[0]= le.transform(list2[0])
    list2=rb.transform(list2)
    list2=pd.DataFrame(list2)
    result=model.predict(list2)
    predection=round(result[0],2)
    sentense="The price of the house is {} lakh ".format(predection)
    
    return render_template("index.html",prediction_text=sentense)
        
        





if __name__ == "__main__":
    app.run()
