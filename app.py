from flask import Flask,render_template,request,jsonify
import pickle
import numpy as np
import pandas as pd
app=Flask(__name__)

car=pd.read_csv('Clean_Extract.csv')
model=pickle.load(open('RandomForestRegressionModel.pkl','rb'))

@app.route('/')
def home():
    return(render_template('home.html'))

@app.route('/signup')
def signup():
    return(render_template('index.html'))

@app.route('/car',methods=['GET','POST'])
def cars():
    companies=sorted(car['company'].unique())
    car_models=sorted(car['full_name'].unique())
    year=sorted(car['year'].unique(),reverse=True)
    fuel_type=car['fuel_type'].unique()
    owner_type=car['owner_type'].unique()
    transmission_type=car['transmission_type'].unique()


    return render_template('car.html',companies=companies, car_models=car_models, years=year,fuel_types=fuel_type,owner_types=owner_type,transmission_types=transmission_type)

# @app.route('/predict_api', methods=['POST'])
# def predict():
#         data=request.json['data']
#         print(data)
#         new_data=np.array(list(data.values())).reshape(1,7)
#         prediction=model.predict(new_data)
#         print(prediction[0])
#         return jsonify(prediction[0])

@app.route('/predict',methods=['POST'])
def predict():
     car_model=request.form.get('car_models')
     company=request.form.get('company')
     year=request.form.get('year')
     driven=request.form.get('kilo_driven')
     owner=request.form.get('owner_type')
     fuel_type=request.form.get('fuel_type')
     transmission=request.form.get('transmission_type')

     prediction=model.predict(pd.DataFrame(columns=['full_name', 'company', 'year', 'km_driven','owner_type', 'fuel_type', 'transmission_type'],
                              data=np.array([car_model,company,year,driven,owner,fuel_type,transmission]).reshape(1, 7)))
     
     return render_template("predictionpage.html",prediction_text="₹ {}".format(str(np.round(prediction[0],2))), company = company.lower(), car_model = car_model.lower())
     

if __name__=='__main__':
    app.run()