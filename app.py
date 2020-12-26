#importing Libraries
import numpy as np
import pandas as pd
from flask import Flask,request,jsonify,render_template
import pickle
import os

#app name
app = Flask(__name__)

#Loading the saved model
def load_model():
    return pickle.load(open('model.pkl','rb'))


#home page
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    try:
        model=load_model()
        feature=[float(x) for x in request.form.values()]
        features=[np.array(feature)]
        prediction=model.predict(features)
        output=prediction.squeeze()
        if output==0:
            res="No"
        if output==1:
            res="Yes"
    
        return render_template('index.html',prediction_text="Loan Eligibility: {}".format(res))
    except:
        return render_template('index.html',prediction_text="Please fill all the Dialog Box")

if __name__ == "__main__":
    port=int(os.environ.get('PORT',5000))
    app.run(port=port,debug=True,use_reloader=False)