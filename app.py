from flask import Flask,render_template
import pandas as pd
app=Flask(__name__)

car=pd.read_csv('Clean_Extract.csv')

@app.route('/')
def home():
    return(render_template('home.html'))

@app.route('/signup')
def signup():
    return(render_template('index.html'))

@app.route('/car')
def cars():
    companies=sorted(car['company'].unique())
    car_models=sorted(car['full_name'].unique())
    year=sorted(car['year'].unique(),reverse=True)
    fuel_type=car['fuel_type'].unique()
    owner_type=car['owner_type'].unique()
    transmission_type=car['transmission_type'].unique()
    return render_template('car.html',companies=companies, car_models=car_models, years=year,fuel_types=fuel_type,owner_types=owner_type,transmission_types=transmission_type)

if __name__=='__main__':
    app.run()