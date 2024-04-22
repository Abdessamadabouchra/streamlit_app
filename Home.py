import streamlit as st
import pandas as pd
import time as t
@st.cache_data
def upload(data):
   data
st.header('Enter your informations')
st.subheader("please don't enter  wrong infos")

time = st.sidebar.slider("chose your time",14,60,20)
sex = st.sidebar.radio("chose  your sex ",('mal','female'))
first_col, sec_col= st.columns(2)
name = first_col.text_input("enter your name !")
phone= first_col.number_input("enter your phone number !",10)

with sec_col:
    secode_name =st.text_input("enter your secode name !")
    keep_data=  st.checkbox("show data ?")
cont = st.sidebar.empty()    
prog = st.sidebar.empty()
data=st.empty()
data = pd.DataFrame({"temp" : time ,"genre"  : sex  ,"name ":name, "phone ":phone ,"seconde name" :  secode_name},index=[1])

if keep_data and (time and sex and name and phone and secode_name ):
   for i in range(0,100):
     prog.progress(i)
     cont.write(f"{i}%")
     t.sleep(0.005)
   prog.write("mession completed") 
   cont.empty() 
   upload(data)
