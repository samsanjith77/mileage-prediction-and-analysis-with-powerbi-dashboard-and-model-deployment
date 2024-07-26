import streamlit as st
import pandas as pd
import numpy as np
import joblib
from helper import avg_country,cylinder_mpg,company_car

# loading the model and scale into these variable
model=joblib.load('model.joblib')
scale=joblib.load('StandardScaler.joblib')
model2=joblib.load('svm_model.joblib')

# title for the app
st.title("Mileage prediction app")
st.header("Enter the details correctly")

# getting inputs 
cylinder=st.selectbox("choose the cylinder",[3,4,5,6,8])
displacement=st.number_input("Displacement",min_value=0)
hp=st.number_input("Horse power",min_value=30)
weight=st.number_input("Weight",min_value=500)
acc=st.number_input("Acceleration",min_value=0)
#get year input with slider
year=st.slider("Model year",min_value=60,max_value=90,step=1)
# get country name as input and change into numbers for prediction
country_option={"Americans":1,"Europe":2,"Japan":3}
temp_country=st.selectbox("Select the country",list(country_option.keys()))
country=country_option[temp_country]

# creating the dataframe for the input data
input_data=pd.DataFrame({'cylinders':[cylinder],'displacement':[displacement],'horsepower':[hp],
                         'weight':[weight],'acceleration':[acc],
                         'model_year':[year],'origin':[country]})
# Scaling the data
data=scale.transform(input_data)

# prediction button
choice=st.sidebar.selectbox('Models',[1,2])

if st.button('Predict Mileage'):
    if(choice==2):
        prediction = model2.predict(data)
        st.success(f'Predicted Mileage: {prediction[0]:.2f}')
        st.balloons()
    else:
        prediction = model.predict(data)
        st.success(f'Predicted Mileage: {prediction[0]:.2f}')
        st.balloons()


# creating graphs 
st.subheader('Graphs')

tab1,tab2,tab3=st.tabs(['average-mpg with countries','Cylinder with mileage','company wise car manufactured'])
#
with tab1:
    cm=st.selectbox("select",['America','Europe','Japan'])
    gg=avg_country(cm)
    st.plotly_chart(gg)

with tab2:
    ll=cylinder_mpg()
    st.plotly_chart(ll)
with tab3:
    rr=company_car()
    
    st.plotly_chart(rr)
