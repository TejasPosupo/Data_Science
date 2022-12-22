from flask import Flask ,render_template
import pandas as pd
app=Flask(__name__)
Car = pd.read_csv('Cleaned Car.csv')
@app.route('/')
def index():
    companies = sorted(Car['company'].unique())
    Car_models = sorted(Car['name'].unique())
    year = sorted(Car['year'].unique(),reverse=True)
    fuel_type = Car['fuel_type'].unique()
    return render_template('index.html', companies=companies, Car_models=Car_models, year=year,fuel_type= fuel_type)
if __name__=='__main__':
    app.run(debug=True)