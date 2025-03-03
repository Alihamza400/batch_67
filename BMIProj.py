import streamlit as st
st.header("BMI  CALCULATER");
body_mass = 1;
def BMI():
    Height = (st.number_input("Enter Height : "));
    Weight = (st.number_input("Enter Your Weight :"));
    st.write("Weight is ",{Weight});
    st.write("Height is ",{Height});
    body_mass = Weight/Height**2;
    st.write("BMI is = ",{body_mass});
BMI();
def check():
    if(body_mass<17):
        st.write("BMI is less");
    elif(body_mass>18 and body_mass<=24):
        st.write("BMI normal");
    else:
        st.write("BMI is Over");
check();